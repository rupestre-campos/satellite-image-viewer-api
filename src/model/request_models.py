from pydantic import BaseModel
import json
class GeoJSONGeometry(BaseModel):
    type: str
    coordinates: list

class SearchImageRequest(BaseModel):
    geometry: GeoJSONGeometry
    parameters: dict

    class Config:
        json_schema_extra = {
            "example": {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [ [
                        [ -47.458665918360282, -1.80123571919746 ],
                        [ -47.458608682448038, -1.799604495698615 ],
                        [ -47.437660338568143, -1.800749213943418 ],
                        [ -47.437760501414559, -1.802552145178983 ],
                        [ -47.458665918360282, -1.80123571919746 ]
                    ] ]
                },
                "parameters": {
                    "max_cloud_coverage": 30,
                    "start_date": "2023-01-01",
                    "end_date": "2024-01-01",
                    "max_results": 5
                }
            }
        }

class RenderImageRequest(BaseModel):
    geometry: GeoJSONGeometry
    parameters: dict

    class Config:
        json_schema_extra = {
            "example": {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [ [
                        [ -47.458665918360282, -1.80123571919746 ],
                        [ -47.458608682448038, -1.799604495698615 ],
                        [ -47.437660338568143, -1.800749213943418 ],
                        [ -47.437760501414559, -1.802552145178983 ],
                        [ -47.458665918360282, -1.80123571919746 ]
                    ] ]
                },
                "parameters": {
                    "zip_file": "N",
                    "image_format": "PNG",
                    "stac_items": [json.loads('''{
                        "type": "Feature",
                        "stac_version": "1.0.0",
                        "id": "S2B_22MHD_20230912_0_L2A",
                        "properties": {
                            "created": "2023-09-12T23:04:12.344Z",
                            "platform": "sentinel-2b",
                            "constellation": "sentinel-2",
                            "instruments": [
                            "msi"
                            ],
                            "eo:cloud_cover": 1.286568,
                            "proj:epsg": 32722,
                            "mgrs:utm_zone": 22,
                            "mgrs:latitude_band": "M",
                            "mgrs:grid_square": "HD",
                            "grid:code": "MGRS-22MHD",
                            "view:sun_azimuth": 75.2632932368365,
                            "view:sun_elevation": 68.1072215742447,
                            "s2:degraded_msi_data_percentage": 0.0171,
                            "s2:nodata_pixel_percentage": 0.000003,
                            "s2:saturated_defective_pixel_percentage": 0,
                            "s2:dark_features_percentage": 0.007405,
                            "s2:cloud_shadow_percentage": 1.452165,
                            "s2:vegetation_percentage": 91.167539,
                            "s2:not_vegetated_percentage": 4.22273,
                            "s2:water_percentage": 1.634059,
                            "s2:unclassified_percentage": 0.229525,
                            "s2:medium_proba_clouds_percentage": 0.923315,
                            "s2:high_proba_clouds_percentage": 0.362836,
                            "s2:thin_cirrus_percentage": 0.000418,
                            "s2:snow_ice_percentage": 0,
                            "s2:product_type": "S2MSI2A",
                            "s2:processing_baseline": "05.09",
                            "s2:product_uri": "S2B_MSIL2A_20230912T133839_N0509_R124_T22MHD_20230912T174059.SAFE",
                            "s2:generation_time": "2023-09-12T17:40:59.000000Z",
                            "s2:datatake_id": "GS2B_20230912T133839_034041_N05.09",
                            "s2:datatake_type": "INS-NOBS",
                            "s2:datastrip_id": "S2B_OPER_MSI_L2A_DS_2BPS_20230912T174059_S20230912T133836_N05.09",
                            "s2:granule_id": "S2B_OPER_MSI_L2A_TL_2BPS_20230912T174059_A034041_T22MHD_N05.09",
                            "s2:reflectance_conversion_factor": 0.985729174026567,
                            "datetime": "2023-09-12T13:42:47.536000Z",
                            "s2:sequence": "0",
                            "earthsearch:s3_path": "s3://sentinel-cogs/sentinel-s2-l2a-cogs/22/M/HD/2023/9/S2B_22MHD_20230912_0_L2A",
                            "earthsearch:payload_id": "roda-sentinel2/workflow-sentinel2-to-stac/65778584c188012777b36a9da5375115",
                            "earthsearch:boa_offset_applied": true,
                            "processing:software": {
                            "sentinel2-to-stac": "0.1.1"
                            },
                            "updated": "2023-09-12T23:04:12.344Z"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                            [
                                [
                                -48.304814333806114,
                                -0.9033707970044846
                                ],
                                [
                                -48.30368051135934,
                                -1.895634898797302
                                ],
                                [
                                -47.31796900571461,
                                -1.8938076637513737
                                ],
                                [
                                -47.319515351230564,
                                -0.9025002577854422
                                ],
                                [
                                -48.304814333806114,
                                -0.9033707970044846
                                ]
                            ]
                            ]
                        },
                        "links": [
                            {
                            "rel": "self",
                            "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2B_22MHD_20230912_0_L2A",
                            "type": "application/geo+json"
                            },
                            {
                            "rel": "canonical",
                            "href": "s3://sentinel-cogs/sentinel-s2-l2a-cogs/22/M/HD/2023/9/S2B_22MHD_20230912_0_L2A/S2B_22MHD_20230912_0_L2A.json",
                            "type": "application/json"
                            },
                            {
                            "rel": "license",
                            "href": "https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice"
                            },
                            {
                            "rel": "derived_from",
                            "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/items/S2B_22MHD_20230912_0_L1C",
                            "type": "application/geo+json"
                            },
                            {
                            "rel": "parent",
                            "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                            "type": "application/json"
                            },
                            {
                            "rel": "collection",
                            "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                            "type": "application/json"
                            },
                            {
                            "rel": "root",
                            "href": "https://earth-search.aws.element84.com/v1",
                            "type": "application/json",
                            "title": "Earth Search by Element 84"
                            },
                            {
                            "rel": "thumbnail",
                            "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2B_22MHD_20230912_0_L2A/thumbnail"
                            }
                        ],
                        "assets": {
                            "blue": {
                            "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/22/M/HD/2023/9/S2B_22MHD_20230912_0_L2A/B02.tif",
                            "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                            "title": "Blue (band 2) - 10m",
                            "eo:bands": [
                                {
                                "name": "blue",
                                "common_name": "blue",
                                "description": "Blue (band 2)",
                                "center_wavelength": 0.49,
                                "full_width_half_max": 0.098
                                }
                            ],
                            "gsd": 10,
                            "proj:shape": [
                                10980,
                                10980
                            ],
                            "proj:transform": [
                                10,
                                0,
                                799980,
                                0,
                                -10,
                                9900040
                            ],
                            "raster:bands": [
                                {
                                "nodata": 0,
                                "data_type": "uint16",
                                "bits_per_sample": 15,
                                "spatial_resolution": 10,
                                "scale": 0.0001,
                                "offset": -0.1
                                }
                            ],
                            "roles": [
                                "data",
                                "reflectance"
                            ]
                            },
                            "green": {
                            "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/22/M/HD/2023/9/S2B_22MHD_20230912_0_L2A/B03.tif",
                            "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                            "title": "Green (band 3) - 10m",
                            "eo:bands": [
                                {
                                "name": "green",
                                "common_name": "green",
                                "description": "Green (band 3)",
                                "center_wavelength": 0.56,
                                "full_width_half_max": 0.045
                                }
                            ],
                            "gsd": 10,
                            "proj:shape": [
                                10980,
                                10980
                            ],
                            "proj:transform": [
                                10,
                                0,
                                799980,
                                0,
                                -10,
                                9900040
                            ],
                            "raster:bands": [
                                {
                                "nodata": 0,
                                "data_type": "uint16",
                                "bits_per_sample": 15,
                                "spatial_resolution": 10,
                                "scale": 0.0001,
                                "offset": -0.1
                                }
                            ],
                            "roles": [
                                "data",
                                "reflectance"
                            ]
                            },
                            "nir": {
                            "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/22/M/HD/2023/9/S2B_22MHD_20230912_0_L2A/B08.tif",
                            "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                            "title": "NIR 1 (band 8) - 10m",
                            "eo:bands": [
                                {
                                "name": "nir",
                                "common_name": "nir",
                                "description": "NIR 1 (band 8)",
                                "center_wavelength": 0.842,
                                "full_width_half_max": 0.145
                                }
                            ],
                            "gsd": 10,
                            "proj:shape": [
                                10980,
                                10980
                            ],
                            "proj:transform": [
                                10,
                                0,
                                799980,
                                0,
                                -10,
                                9900040
                            ],
                            "raster:bands": [
                                {
                                "nodata": 0,
                                "data_type": "uint16",
                                "bits_per_sample": 15,
                                "spatial_resolution": 10,
                                "scale": 0.0001,
                                "offset": -0.1
                                }
                            ],
                            "roles": [
                                "data",
                                "reflectance"
                            ]
                            },
                            "red": {
                            "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/22/M/HD/2023/9/S2B_22MHD_20230912_0_L2A/B04.tif",
                            "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                            "title": "Red (band 4) - 10m",
                            "eo:bands": [
                                {
                                "name": "red",
                                "common_name": "red",
                                "description": "Red (band 4)",
                                "center_wavelength": 0.665,
                                "full_width_half_max": 0.038
                                }
                            ],
                            "gsd": 10,
                            "proj:shape": [
                                10980,
                                10980
                            ],
                            "proj:transform": [
                                10,
                                0,
                                799980,
                                0,
                                -10,
                                9900040
                            ],
                            "raster:bands": [
                                {
                                "nodata": 0,
                                "data_type": "uint16",
                                "bits_per_sample": 15,
                                "spatial_resolution": 10,
                                "scale": 0.0001,
                                "offset": -0.1
                                }
                            ],
                            "roles": [
                                "data",
                                "reflectance"
                            ]
                            }
                        },
                        "bbox": [
                            -48.304814333806114,
                            -1.895634898797302,
                            -47.31796900571461,
                            -0.9025002577854422
                        ],
                        "stac_extensions": [
                            "https://stac-extensions.github.io/view/v1.0.0/schema.json",
                            "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
                            "https://stac-extensions.github.io/mgrs/v1.0.0/schema.json",
                            "https://stac-extensions.github.io/projection/v1.1.0/schema.json",
                            "https://stac-extensions.github.io/grid/v1.0.0/schema.json",
                            "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
                            "https://stac-extensions.github.io/processing/v1.1.0/schema.json"
                        ],
                        "collection": "sentinel-2-l2a"
                        }''')],
                }
            }
        }
