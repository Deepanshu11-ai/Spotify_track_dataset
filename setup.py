import os

# Root project folder
project_name = "Project"

# Folder structure
folders = [
    "config",
    "data/raw",
    "data/interim",
    "data/processed",
    "data/external",
    "artifacts/data_ingestion",
    "artifacts/data_validation",
    "artifacts/data_transformation",
    "artifacts/model_trainer",
    "artifacts/model_evaluation",
    "artifacts/model_pusher",
    "src/components",
    "src/pipeline",
    "src/config",
    "src/entity",
    "src/utils",
    "src/constants",
    "models",
    "notebooks",
    "logs"
]

# Files to create
files = [
    "config/config.yaml",
    "config/schema.yaml",
    "config/paths.yaml",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/components/model_pusher.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/config/configuration.py",
    "src/entity/config_entity.py",
    "src/entity/artifact_entity.py",
    "src/utils/common.py",
    "src/utils/logger.py",
    "src/utils/exception.py",
    "src/constants/__init__.py",
    "models/trained_model.pkl",
    "notebooks/experimentation.ipynb",
    "app.py",
    "requirements.txt",
    "setup.py",
    "README.md"
]

def create_structure():
    # Create root folder
    os.makedirs(project_name, exist_ok=True)

    # Create folders
    for folder in folders:
        folder_path = os.path.join(project_name, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Create files
    for file in files:
        file_path = os.path.join(project_name, file)
        dir_name = os.path.dirname(file_path)

        if not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "w") as f:
            pass  # creates empty file

    print(f"\n✅ Project structure '{project_name}' created successfully!")

if __name__ == "__main__":
    create_structure()