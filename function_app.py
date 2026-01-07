import azure.functions as func
import logging

# Import all blueprints
from radarpipeline.ingestion.function_ingest import bp as ingest_bp
from radarpipeline.extraction.function_extraction import bp as extraction_bp
from radarpipeline.preview.function_preview_users import bp as preview_users_bp
from radarpipeline.storage.function_store import bp as storage_bp

app = func.FunctionApp()
logger = logging.getLogger(__name__)

# Register blueprints
app.register_functions(ingest_bp)
app.register_functions(extraction_bp)
app.register_functions(preview_users_bp)
app.register_functions(storage_bp)
