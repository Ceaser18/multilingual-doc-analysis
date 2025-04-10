import os
from kaggle.api.kaggle_api_extended import KaggleApi
from datasets import load_dataset

def download_kaggle_dataset(dataset_path, download_dir):
    api = KaggleApi()
    api.authenticate()

    dataset_name = dataset_path.split("/")[-1]
    target_path = os.path.join(download_dir, dataset_name)

    if not os.path.exists(target_path):
        print(f"Downloading Kaggle dataset: {dataset_path}")
        api.dataset_download_files(dataset_path, path=target_path, unzip=True)
    else:
        print(f"Kaggle dataset already exists at: {target_path}")

def download_huggingface_dataset(dataset_name, config=None, trust_code=False):
    try:
        if config:
            dataset = load_dataset(dataset_name, config, trust_remote_code=trust_code)
        else:
            dataset = load_dataset(dataset_name, trust_remote_code=trust_code)
        print(f"✅ Downloaded HuggingFace dataset: {dataset_name} (config: {config if config else 'default'})")
    except Exception as e:
        print(f"❌ Failed to download {dataset_name}: {e}")

if __name__ == "__main__":
    # Use the 'raw' folder in your project directory
    kaggle_dir = os.path.join(os.getcwd(), "raw")

    kaggle_datasets = [
        "datasnaek/youtube-new",                     # YouTube Trending
        "clmentbisaillon/fake-and-real-news-dataset"  # Fake and Real News
    ]

    for ds in kaggle_datasets:
        download_kaggle_dataset(ds, kaggle_dir)

    # Updated HuggingFace datasets: only English content
    huggingface_datasets = [
        ("xnli", "en", False)  # Download only the English part of XNLI
        # Add other English-only HuggingFace datasets here as needed
    ]

    for ds, config, trust in huggingface_datasets:
        download_huggingface_dataset(ds, config, trust)
