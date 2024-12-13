from google.cloud import storage
from google.oauth2 import service_account
import os

PROJECT_ID = "striped-graph-440017-d7"

# Initialize GCS client using Application Default Credentials (ADC)
client = storage.Client(project=PROJECT_ID)

def list_buckets_and_structure(output_file="gcpbuckettree.txt"):
    """Lists all buckets and their folder structures, saving the output to a file."""
    with open(output_file, "w") as f:
        # List all buckets
        buckets = client.list_buckets()
        for bucket in buckets:
            f.write(f"Bucket: {bucket.name}\n")
            print(f"Bucket: {bucket.name}")
            list_bucket_tree(bucket, f)
            f.write("\n\n")

def list_bucket_tree(bucket, file_handle):
    """Recursively lists objects within a bucket to create a tree structure."""
    blobs = client.list_blobs(bucket.name)
    tree_structure = {}

    # Build a dictionary to represent the folder structure
    for blob in blobs:
        parts = blob.name.split("/")
        current_level = tree_structure
        for part in parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]

    # Write the tree structure to the file
    def write_tree(structure, indent=0):
        for key, sub_structure in structure.items():
            file_handle.write("  " * indent + f"{key}\n")
            print("  " * indent + f"{key}")  # Print to console for verification
            write_tree(sub_structure, indent + 1)

    write_tree(tree_structure)


list_buckets_and_structure("gcpbuckettree.txt")
