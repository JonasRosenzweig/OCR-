#from https://github.com/szeamer/google-cloud-vision-script/blob/main/script.py
import json
import os
import re
from google.cloud import vision, storage

# get credentials
credentials ="C:/Users/surface/Desktop/YouWe/OCR Project/fine-sublime-319610-dc80d5c6f639.json"


def async_detect_document(gcs_source_uri, gcs_destination_uri):
    # Supported mime_types are: 'application/pdf' and 'image/tiff'
    mime_type = 'application/pdf'

    # How many pages should be grouped into each json output file.
    batch_size = 100

    client = vision.ImageAnnotatorClient(credentials=credentials)

    feature = vision.Feature(
        type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)

    gcs_source = vision.GcsSource(uri=gcs_source_uri)
    input_config = vision.InputConfig(
        gcs_source=gcs_source, mime_type=mime_type)

    gcs_destination = vision.GcsDestination(uri=gcs_destination_uri)
    output_config = vision.OutputConfig(
        gcs_destination=gcs_destination, batch_size=batch_size)

    async_request = vision.AsyncAnnotateFileRequest(
        features=[feature], input_config=input_config,
        output_config=output_config)

    operation = client.async_batch_annotate_files(
        requests=[async_request])

    print('Waiting for the operation to finish.')
    operation.result(timeout=420)


def write_to_text(gcs_destination_uri):
    # Once the request has completed and the output has been
    # written to GCS, we can list all the output files.
    storage_client = storage.Client()

    match = re.match(r'gs://([^/]+)/(.+)', gcs_destination_uri)
    bucket_name = match.group(1)
    prefix = match.group(2)

    bucket = storage_client.get_bucket(bucket_name)

    # List objects with the given prefix.
    blob_list = list(bucket.list_blobs(prefix=prefix))
    print('Output files:')

    transcription = open("transcription.txt", "w")

    for blob in blob_list:
        print(blob.name)

    # Process the first output file from GCS.
    # Since we specified batch_size=2, the first response contains
    # the first two pages of the input file.
    for n in range(len(blob_list)):
        output = blob_list[n]

        json_string = output.download_as_string()
        response = json.loads(json_string)

        # The actual response for the first page of the input file.
        for m in range(len(response['responses'])):

            first_page_response = response['responses'][m]

            try:
                annotation = first_page_response['fullTextAnnotation']
            except(KeyError):
                print("No annotation for this page.")

            # Here we print the full text from the first page.
            # The response contains more information:
            # annotation/pages/blocks/paragraphs/words/symbols
            # including confidence scores and bounding boxes
            print('Full text:\n')
            print(annotation['text'])

            with open("transcription.txt", "a+", encoding="utf-8") as f:
                f.write(annotation['text'])


async_detect_document('gs://batching_test_data/pdf/13370636.pdf', 'gs://Google Vision/text')
write_to_text('gs://Google Vision/text')