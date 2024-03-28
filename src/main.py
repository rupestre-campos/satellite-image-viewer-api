import io
import json
import numpy as np
from PIL import Image
from datetime import datetime
from fastapi import (
    FastAPI,
    HTTPException,
    Request,
    Response
)
from fastapi.responses import JSONResponse


from app_config import AppConfig
from controller.image_renderer import ImageRenderer
from controller.catalog_searcher import CatalogSearcher
from model.request_models import (
    RenderImageRequest,
    SearchImageRequest,
)

app = FastAPI()
app_config_data = AppConfig()

image_formats_mimes = {
    "PNG": "image/png",
    "JPEG": "image/jpeg"
}


@app.get("/health")
async def health_check():
    return {"status": "OK"}


@app.post("/search-image")
async def search_image(request: SearchImageRequest):
    geometry = request.geometry
    parameters = request.parameters
    # Extracting parameters
    max_cloud_coverage = parameters.get("max_cloud_coverage", 10)
    start_date_str = parameters.get("start_date", datetime(2015, 6, 22).strftime("%Y-%m-%d"))
    end_date_str = parameters.get("end_date", datetime.now().strftime("%Y-%m-%d"))
    max_results = parameters.get("max_results", 5)
    # Parsing dates
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except TypeError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    date_string = f"{start_date.strftime('%Y-%m-%d')}/{end_date.strftime('%Y-%m-%d')}"
    catalog_worker = CatalogSearcher(
        app_config_data.stac_url,
        feature_geojson=geometry.dict(),
        date_string=date_string,
        max_cloud_cover=max_cloud_coverage,
        max_items=max_results
    )
    stac_items = catalog_worker.search_images()

    search_result = {"images_found": len(stac_items), "items": stac_items}
    return search_result


@app.post("/render-image")
async def render_image(request: RenderImageRequest):
    geometry = request.geometry
    parameters = request.parameters
    stac_list = parameters.get("stac_items", {})
    image_format = parameters.get("image_format", "PNG")
    zip_file = parameters.get("zip_file", "N")
    if len(stac_list)==0:
        raise HTTPException(status_code=400, detail="Empty stac list.")
    if image_format not in image_formats_mimes:
        raise HTTPException(status_code=400, detail="Image format invalid.")

    renderer = ImageRenderer(
        stac_list=stac_list,
        geojson_geometry=geometry.model_dump(),
        image_format=image_format
    )
    if zip_file == "N":
        image_data = renderer.render_mosaic_from_stac(zip_file=False)
        return Response(
            content=image_data["image"],
            media_type=image_formats_mimes.get(image_format)
        )

    image_data = renderer.render_mosaic_from_stac(zip_file=True)
    return Response(
        content=image_data["zip_file"],
        media_type="application/octet-stream"
    )


# Custom exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )
