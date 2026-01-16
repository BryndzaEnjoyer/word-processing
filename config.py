from pathlib import Path

def get_data_file_path(filename):
	return Path(__file__).parent / "data/raw" / filename

def get_output_file_path(filename):
	return Path(__file__).parent / "data/processed" / filename
