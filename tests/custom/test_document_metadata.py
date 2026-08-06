from pulse import DocumentMetadataResult
from pulse.core.jsonable_encoder import jsonable_encoder
from pulse.core.unchecked_base_model import construct_type
from pulse.types import (
    ExtractAsyncRequestExtensions,
    ExtractInputExtensions,
    ExtractOptionsExtensions,
    ExtractRequestExtensions,
    ExtractResponse,
    PipelineStepBatchExtractConfigExtensions,
)


def test_document_metadata_uses_snake_case_wire_key_across_extract_inputs() -> None:
    extension_types = (
        ExtractRequestExtensions,
        ExtractAsyncRequestExtensions,
        ExtractInputExtensions,
        ExtractOptionsExtensions,
        PipelineStepBatchExtractConfigExtensions,
    )

    for extension_type in extension_types:
        encoded = jsonable_encoder(extension_type(document_metadata=True))
        assert encoded["document_metadata"] is True
        assert "documentMetadata" not in encoded


def test_extract_response_parses_typed_document_metadata() -> None:
    response = construct_type(
        type_=ExtractResponse,
        object_={
            "markdown": "# Metadata fixture",
            "extensions": {
                "document_metadata": {
                    "file": {
                        "name": "pulse-complex-metadata-10-page.pdf",
                        "extension": ".pdf",
                        "media_type": "application/pdf",
                        "size_bytes": 32506,
                    },
                    "properties": {
                        "title": "Pulse Complex Metadata Validation Report",
                        "authors": ["Ritvik Pandey", "Pulse Document Intelligence"],
                        "application_version": "16.0",
                    },
                    "custom": {"PulseCaseId": "PULSE-META-10P-2026"},
                    "structure": {
                        "page_count": 10,
                        "outline_count": 10,
                        "attachment_count": 1,
                        "annotation_types": {"Link": 3},
                        "active_sheet": "Summary",
                        "embedded_image_count": 2,
                    },
                    "format_specific": {"pdf_version": "1.7", "encrypted": False},
                    "warnings": [],
                }
            },
        },
    )

    assert response.extensions is not None
    metadata = response.extensions.document_metadata
    assert isinstance(metadata, DocumentMetadataResult)
    assert metadata.file.media_type == "application/pdf"
    assert metadata.properties.authors == ["Ritvik Pandey", "Pulse Document Intelligence"]
    assert metadata.properties.application_version == "16.0"
    assert metadata.structure.page_count == 10
    assert metadata.structure.outline_count == 10
    assert metadata.structure.annotation_types == {"Link": 3}
    assert metadata.structure.active_sheet == "Summary"
    assert metadata.structure.embedded_image_count == 2
    assert metadata.custom == {"PulseCaseId": "PULSE-META-10P-2026"}
    assert metadata.format_specific == {"pdf_version": "1.7", "encrypted": False}
    assert metadata.warnings == []
