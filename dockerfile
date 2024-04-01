# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /src

# Copy the current directory contents into the container at /app
COPY ./src /src
COPY requirements.txt /src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

EXPOSE 8000

ENV GDAL_CACHEMAX=200
ENV GDAL_DISABLE_READDIR_ON_OPEN=EMPTY_DIR
ENV GDAL_HTTP_MULTIPLEX=YES
ENV GDAL_HTTP_MERGE_CONSECUTIVE_RANGES=YES
ENV CPL_VSIL_CURL_ALLOWED_EXTENSIONS=".tif,.TIF,.tiff"
ENV VSI_CACHE=TRUE
ENV VSI_CACHE_SIZE=5000000
ENV GDAL_HTTP_VERSION=2
ENV PROJ_NETWORK=OFF

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
