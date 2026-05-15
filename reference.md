# Reference
<details><summary><code>client.<a href="src/pulse/client.py">extract</a>(...) -> ExtractResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The primary endpoint for the Pulse API. Parses uploaded documents or remote
file URLs and returns rich markdown content with optional structured data
extraction based on user-provided schemas and extraction options.

Set `async: true` to return immediately with a job_id for polling via
GET /job/{jobId}. Otherwise processes synchronously.

To process many files at once, see [Batch Extract](api:POST/batch/extract)
or the [Batch Processing guide](/batch).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.extract(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — Document to upload directly. Required unless fileUrl is provided.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — Public or pre-signed URL that Pulse will download and extract. Required unless file is provided.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ExtractRequestModel]` — Extraction model to use. When set to `pulse-ultra-2`, routes the request through Pulse Ultra 2 (self-hosted VPC model) instead of the default cloud-based service. If omitted or set to `default`, the default model is used.
    
</dd>
</dl>

<dl>
<dd>

**extraction_config_id:** `typing.Optional[str]` — UUID of a saved extraction configuration (a "preset"). When provided, the server loads the saved configuration and applies its options on top of any inline parameters supplied in this request. Inline parameters always take precedence over preset values for the same field. Saved configs are managed via the platform UI or the `input_extractions` admin endpoints.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Page range filter supporting segments such as `1-2` or mixed ranges like `1-2,5`.
    
</dd>
</dl>

<dl>
<dd>

**figure_processing:** `typing.Optional[ExtractRequestFigureProcessing]` — Settings that control how figures and embedded visuals are processed. Applies to both PDFs/images (where figures are detected from layout) and spreadsheets (where charts and embedded images are read directly from the workbook). These options affect the markdown output and the `bounding_boxes.Images[]` array; they do not produce additional output fields elsewhere in the response.
    
</dd>
</dl>

<dl>
<dd>

**extensions:** `typing.Optional[ExtractRequestExtensions]` — Settings that enable additional processing passes or alternate output formats. Each enabled extension produces a corresponding output field under `response.extensions.*`.
    
</dd>
</dl>

<dl>
<dd>

**spreadsheet:** `typing.Optional[ExtractRequestSpreadsheet]` — Settings for Excel/spreadsheet extraction. Controls handling of hidden rows, columns, and sheets. Applies to `.xlsx`, `.xlsm`, and `.xls` files. Accepts both camelCase and snake_case field names.
    
</dd>
</dl>

<dl>
<dd>

**storage:** `typing.Optional[ExtractRequestStorage]` — Options for persisting extraction artifacts. When enabled (default), artifacts are saved to storage and a database record is created.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — If true, returns immediately with a job_id for polling via GET /job/{jobId}. Otherwise processes synchronously.
    
</dd>
</dl>

<dl>
<dd>

**structured_output:** `typing.Optional[ExtractRequestStructuredOutput]` — **⚠️ DEPRECATED** — Use the `/schema` endpoint after extraction instead. Pass the `extraction_id` from the extract response to `/schema` with your `schema_config`. This parameter still works for backward compatibility but will be removed in a future version.
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[ExtractRequestSchema]` — (Deprecated) JSON schema describing structured data to extract. Use structuredOutput instead. Accepts either a JSON object or a stringified JSON representation.
    
</dd>
</dl>

<dl>
<dd>

**schema_prompt:** `typing.Optional[str]` — (Deprecated) Natural language prompt for schema-guided extraction. Use structuredOutput.schemaPrompt instead.
    
</dd>
</dl>

<dl>
<dd>

**custom_prompt:** `typing.Optional[str]` — (Deprecated) Custom instructions that augment the default extraction behaviour. Use `figureProcessing` or `extensions` instead.
    
</dd>
</dl>

<dl>
<dd>

**chunking:** `typing.Optional[str]` — **⚠️ DEPRECATED** — Use `extensions.chunking.chunkTypes` instead. Comma-separated list of chunking strategies to apply (for example `semantic,header,page,recursive`). Still accepted for backward compatibility.
    
</dd>
</dl>

<dl>
<dd>

**chunk_size:** `typing.Optional[int]` — **⚠️ DEPRECATED** — Use `extensions.chunking.chunkSize` instead. Override for maximum characters per chunk when chunking is enabled.
    
</dd>
</dl>

<dl>
<dd>

**extract_figure:** `typing.Optional[bool]` — **⚠️ DEPRECATED** — Toggle to enable figure extraction in results.
    
</dd>
</dl>

<dl>
<dd>

**figure_description:** `typing.Optional[bool]` — **⚠️ DEPRECATED** — Use `figureProcessing.description` instead. Toggle to generate descriptive captions for extracted figures.
    
</dd>
</dl>

<dl>
<dd>

**show_images:** `typing.Optional[bool]` — **⚠️ DEPRECATED** — Use `figureProcessing.showImages` instead. Embed base64-encoded images inline in figure tags in the output. Increases response size.
    
</dd>
</dl>

<dl>
<dd>

**return_html:** `typing.Optional[bool]` — **⚠️ DEPRECATED** — Use `extensions.altOutputs.returnHtml` instead. Whether to include HTML representation alongside markdown in the response.
    
</dd>
</dl>

<dl>
<dd>

**thinking:** `typing.Optional[bool]` — (Deprecated) Enables expanded rationale output for debugging.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/pulse/client.py">extract_async</a>(...) -> AsyncSubmissionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Deprecated**: Use `/extract` with `async: true` instead.

Starts an asynchronous extraction job. The request mirrors the
synchronous options but returns immediately with a job identifier that
clients can poll for completion status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.extract_async(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — Document to upload directly. Required unless fileUrl is provided.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — Public or pre-signed URL that Pulse will download and extract. Required unless file is provided.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ExtractAsyncRequestModel]` — Extraction model to use. When set to `pulse-ultra-2`, routes the request through Pulse Ultra 2 (self-hosted VPC model) instead of the default cloud-based service. If omitted or set to `default`, the default model is used.
    
</dd>
</dl>

<dl>
<dd>

**extraction_config_id:** `typing.Optional[str]` — UUID of a saved extraction configuration (a "preset"). When provided, the server loads the saved configuration and applies its options on top of any inline parameters supplied in this request. Inline parameters always take precedence over preset values for the same field. Saved configs are managed via the platform UI or the `input_extractions` admin endpoints.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Page range filter supporting segments such as `1-2` or mixed ranges like `1-2,5`.
    
</dd>
</dl>

<dl>
<dd>

**figure_processing:** `typing.Optional[ExtractAsyncRequestFigureProcessing]` — Settings that control how figures and embedded visuals are processed. Applies to both PDFs/images (where figures are detected from layout) and spreadsheets (where charts and embedded images are read directly from the workbook). These options affect the markdown output and the `bounding_boxes.Images[]` array; they do not produce additional output fields elsewhere in the response.
    
</dd>
</dl>

<dl>
<dd>

**extensions:** `typing.Optional[ExtractAsyncRequestExtensions]` — Settings that enable additional processing passes or alternate output formats. Each enabled extension produces a corresponding output field under `response.extensions.*`.
    
</dd>
</dl>

<dl>
<dd>

**spreadsheet:** `typing.Optional[ExtractAsyncRequestSpreadsheet]` — Settings for Excel/spreadsheet extraction. Controls handling of hidden rows, columns, and sheets. Applies to `.xlsx`, `.xlsm`, and `.xls` files. Accepts both camelCase and snake_case field names.
    
</dd>
</dl>

<dl>
<dd>

**storage:** `typing.Optional[ExtractAsyncRequestStorage]` — Options for persisting extraction artifacts. When enabled (default), artifacts are saved to storage and a database record is created.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — If true, returns immediately with a job_id for polling via GET /job/{jobId}. Otherwise processes synchronously.
    
</dd>
</dl>

<dl>
<dd>

**structured_output:** `typing.Optional[ExtractAsyncRequestStructuredOutput]` — **⚠️ DEPRECATED** — Use the `/schema` endpoint after extraction instead. Pass the `extraction_id` from the extract response to `/schema` with your `schema_config`. This parameter still works for backward compatibility but will be removed in a future version.
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[ExtractAsyncRequestSchema]` — (Deprecated) JSON schema describing structured data to extract. Use structuredOutput instead. Accepts either a JSON object or a stringified JSON representation.
    
</dd>
</dl>

<dl>
<dd>

**schema_prompt:** `typing.Optional[str]` — (Deprecated) Natural language prompt for schema-guided extraction. Use structuredOutput.schemaPrompt instead.
    
</dd>
</dl>

<dl>
<dd>

**custom_prompt:** `typing.Optional[str]` — (Deprecated) Custom instructions that augment the default extraction behaviour. Use `figureProcessing` or `extensions` instead.
    
</dd>
</dl>

<dl>
<dd>

**chunking:** `typing.Optional[str]` — **⚠️ DEPRECATED** — Use `extensions.chunking.chunkTypes` instead. Comma-separated list of chunking strategies to apply (for example `semantic,header,page,recursive`). Still accepted for backward compatibility.
    
</dd>
</dl>

<dl>
<dd>

**chunk_size:** `typing.Optional[int]` — **⚠️ DEPRECATED** — Use `extensions.chunking.chunkSize` instead. Override for maximum characters per chunk when chunking is enabled.
    
</dd>
</dl>

<dl>
<dd>

**extract_figure:** `typing.Optional[bool]` — **⚠️ DEPRECATED** — Toggle to enable figure extraction in results.
    
</dd>
</dl>

<dl>
<dd>

**figure_description:** `typing.Optional[bool]` — **⚠️ DEPRECATED** — Use `figureProcessing.description` instead. Toggle to generate descriptive captions for extracted figures.
    
</dd>
</dl>

<dl>
<dd>

**show_images:** `typing.Optional[bool]` — **⚠️ DEPRECATED** — Use `figureProcessing.showImages` instead. Embed base64-encoded images inline in figure tags in the output. Increases response size.
    
</dd>
</dl>

<dl>
<dd>

**return_html:** `typing.Optional[bool]` — **⚠️ DEPRECATED** — Use `extensions.altOutputs.returnHtml` instead. Whether to include HTML representation alongside markdown in the response.
    
</dd>
</dl>

<dl>
<dd>

**thinking:** `typing.Optional[bool]` — (Deprecated) Enables expanded rationale output for debugging.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/pulse/client.py">split</a>(...) -> SplitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Identify which pages of a document contain each topic/section.
Takes an existing extraction and a list of topics, then uses AI to
identify which PDF pages contain content related to each topic.

The result is persisted with a `split_id` that can be used with
the `/schema` endpoint (split mode) for targeted schema extraction on
specific page groups.

Set `async: true` to return immediately with a job_id for polling.

To split many extractions at once, see [Batch Split](api:POST/batch/split)
or the [Batch Processing guide](/batch).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.split(
    extraction_id="extraction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extraction_id:** `str` — ID of the saved extraction to split.
    
</dd>
</dl>

<dl>
<dd>

**split_config:** `typing.Optional[SplitConfig]` — Inline split configuration with topics. Required if split_config_id is not provided.
    
</dd>
</dl>

<dl>
<dd>

**split_config_id:** `typing.Optional[str]` — Reference to a saved split configuration. Use this instead of providing split_config inline.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — If true, returns immediately with a job_id for polling via  GET /job/{jobId}. Otherwise processes synchronously.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/pulse/client.py">schema</a>(...) -> SchemaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply schema extraction to a previously saved extraction. The mode is
inferred from the input:

**Single mode** — Provide `extraction_id` + `schema_config` (or
`schema_config_id`) to apply one schema to the entire document.

**Multi-extraction mode** — Provide a batch extract ID as `extraction_id`
(auto-detected) or an explicit `extraction_ids` list. The content from all
extractions is combined and the schema is applied to the composite. Citations
use `extraction_id-bb_id` format to disambiguate across source documents.

**Split mode** — Provide `split_id` + `split_schema_config` to apply
different schemas to different page groups from a prior `/split` call.
Each topic can have its own schema, prompt, and effort setting.

**Excel template mode** — Provide `excel_template` (base64 .xlsx) in
`schema_config` instead of `input_schema`. The schema is auto-generated
from the template's column headers, and a filled copy is returned as
`excel_output_url`.

Creates a versioned schema record that can be retrieved later.
Set `async: true` to return immediately with a job_id for polling.

To apply schemas across many extractions or splits at once, see
[Batch Schema](api:POST/batch/schema) or the
[Batch Processing guide](/batch).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.schema()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extraction_id:** `typing.Optional[str]` — ID of a saved extraction OR a batch extract job. When a batch extract ID is provided, the system auto-detects it and combines all completed child extractions into a single schema application.
    
</dd>
</dl>

<dl>
<dd>

**extraction_ids:** `typing.Optional[typing.List[str]]` — Explicit list of extraction IDs to combine. The markdown and bounding boxes from all extractions are merged and the schema is applied to the composite content. Citations use `extraction_id-bb_id` format to disambiguate across source documents.
    
</dd>
</dl>

<dl>
<dd>

**split_id:** `typing.Optional[str]` — ID of saved split (from a prior `/split` call). Use for split-mode schema extraction.
    
</dd>
</dl>

<dl>
<dd>

**schema_config:** `typing.Optional[SchemaConfig]` — Inline schema configuration for single mode. Required (with extraction_id) if schema_config_id is not provided.
    
</dd>
</dl>

<dl>
<dd>

**schema_config_id:** `typing.Optional[str]` — Reference to a saved schema configuration for single mode. Use this instead of providing schema_config inline.
    
</dd>
</dl>

<dl>
<dd>

**split_schema_config:** `typing.Optional[typing.Dict[str, TopicSchemaConfig]]` — Per-topic schema configurations for split mode. Keys must match the topic names from the split. Each topic provides either inline schema or schema_config_id.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — If true, returns immediately with a job_id for polling via  GET /job/{jobId}. Otherwise processes synchronously.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/pulse/client.py">download_schema_excel</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the filled Excel template produced by a schema extraction that
used `excel_template` in its `schema_config`. Requires the same API key
authentication as other endpoints. The caller must belong to the org
that owns the underlying extraction.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.download_schema_excel(
    schema_id="schemaId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `str` — The schema ID returned from a prior `POST /schema` call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/pulse/client.py">tables</a>(...) -> TablesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extract tables from a previously completed extraction. Processes the
extraction's document content and returns structured table data.

Requires the `tables_endpoint` feature flag to be enabled for your
organization.

Set `async: true` to return immediately with a `tables_id` for
polling via `GET /job/{tables_id}`.

To extract tables from many extractions at once, see
[Batch Tables](api:POST/batch/tables) or the
[Batch Processing guide](/batch).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.tables(
    extraction_id="extraction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extraction_id:** `str` — ID of a completed extraction to extract tables from.
    
</dd>
</dl>

<dl>
<dd>

**tables_config:** `typing.Optional[TablesConfig]` — Table extraction configuration. If omitted, defaults are used (`merge: false`, `table_format: "html"`).
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — When true, returns immediately with a job ID. Poll `GET /job/{tables_id}` for the result.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Form
<details><summary><code>client.form.<a href="src/pulse/form/client.py">detect</a>(...) -> FormResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run cell detection on a PDF and return the detected `form_fields`
along with a reusable `form_id`. No LLM matching, no fill, no
clear — this is the OCR / layout step that `/form/fill` and
`/form/clear` would otherwise run internally.

The returned `form_id` references the uploaded PDF and its
detected layout, and can be passed back to a subsequent
`/form/fill`, `/form/clear`, or `/form/detect` call as the
single input source — Pulse will skip detection on the fast
path and reuse the cached cells.

**Input modes** — provide exactly one of:
- `form_id` — re-detect cells on a previously stored PDF.
  Useful when callers want to refresh layout after editing or
  when chaining detect calls.
- `file_url` — public or pre-signed URL Pulse will download.
- `file` — direct binary upload of the PDF.

All three input modes ride on the same `multipart/form-data`
request body. (Callers sending `Content-Type: application/json`
with `form_id` / `file_url` are still accepted server-side for
backward compatibility, but the SDKs only model the multipart
form.)

Optional `page_range` (alias `pages`, e.g. `"1-3,5"`) restricts
the operation to a subset of pages.

Synchronous by default — returns the detected layout inline.
Set `async: true` to receive `{job_id, status: "pending"}`
immediately and poll [GET /job/{jobId}](api:GET/job/{jobId}).

Billed at **1 credit per page**. Requires the `form_filler`
feature flag to be enabled for your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.form.detect(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — Direct binary upload of the PDF. Mutually exclusive with `file_url` and `form_id`.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — Public or pre-signed URL of a PDF Pulse will download. Mutually exclusive with `file` and `form_id`.
    
</dd>
</dl>

<dl>
<dd>

**form_id:** `typing.Optional[str]` — Reference to a previously processed form. Mutually exclusive with `file` / `file_url`.
    
</dd>
</dl>

<dl>
<dd>

**page_range:** `typing.Optional[str]` — Restrict the operation to a subset of pages, e.g. `"1-3,5"`.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[str]` — Set to `"true"` to run asynchronously and receive `{job_id, status}` immediately.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.form.<a href="src/pulse/form/client.py">fill</a>(...) -> FormResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fill the fields of a PDF form with values inferred from a natural
language `instructions` prompt. Works on both AcroForm PDFs
(true form fields are written) and flat/scanned PDFs (values
are rendered as an overlay using detected cells from OCR).

**Input modes** — provide exactly one of:
- `form_id` — reuse a previously processed form from a prior
  `/form/detect`, `/form/fill`, or `/form/clear` call. Skips
  re-detection (fast path); the cached `form_fields` are
  reused.
- `file_url` — public or pre-signed URL of a PDF Pulse will
  download.
- `file` — direct binary upload of the PDF. Pulse runs cell
  detection internally before filling.

All three input modes ride on the same `multipart/form-data`
request body. (Callers sending `Content-Type: application/json`
with `form_id` / `file_url` are still accepted server-side for
backward compatibility, but the SDKs only model the multipart
form.)

Optional `form_fields` lets callers supply or edit the detected
cells before filling. Optional `page_range` (alias `pages`,
e.g. `"1-3,5"`) restricts the operation to a subset of pages.

Synchronous by default — returns the filled `FormResult` inline
(including a `pdf_url` you can `GET` to download the PDF
binary). Set `async: true` to receive `{job_id, status:
"pending"}` and poll [GET /job/{jobId}](api:GET/job/{jobId}).

Billed at **3 credits per page**. Requires the `form_filler`
feature flag to be enabled for your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.form.fill(
    file="example_file",
    instructions="instructions",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**instructions:** `str` — Required natural-language fill prompt.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — Direct binary upload of the PDF. Mutually exclusive with `file_url` and `form_id`.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — Public or pre-signed URL of a PDF Pulse will download. Mutually exclusive with `file` and `form_id`.
    
</dd>
</dl>

<dl>
<dd>

**form_id:** `typing.Optional[str]` — Reference to a previously processed form. Mutually exclusive with `file` / `file_url`.
    
</dd>
</dl>

<dl>
<dd>

**form_fields:** `typing.Optional[str]` — Optional JSON-encoded array of `FormCell` objects to override detected cells. Multipart bodies must serialise this field as a string.
    
</dd>
</dl>

<dl>
<dd>

**page_range:** `typing.Optional[str]` — Restrict the operation to a subset of pages, e.g. `"1-3,5"`.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[str]` — Set to `"true"` to run asynchronously and receive `{job_id, status}` immediately.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.form.<a href="src/pulse/form/client.py">clear</a>(...) -> FormResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove user-entered data from a PDF form, leaving the blank
form template intact. Erases handwritten entries, typed values,
and unchecks selected checkboxes — printed labels, field
titles, section headers, and other static template content are
preserved.

**Input modes** — provide exactly one of:
- `form_id` — reuse a previously processed form from a prior
  `/form/detect`, `/form/fill`, or `/form/clear` call (fast
  path; cached layout reused).
- `file_url` — public or pre-signed URL of a PDF Pulse will
  download.
- `file` — direct binary upload of the PDF.

All three input modes ride on the same `multipart/form-data`
request body. (Callers sending `Content-Type: application/json`
with `form_id` / `file_url` are still accepted server-side for
backward compatibility, but the SDKs only model the multipart
form.)

`instructions` is optional. When omitted, Pulse clears every
user-filled field deterministically (no LLM call) on AcroForm
PDFs, eliminating any chance of hallucinated content. Provide
a natural language prompt to clear only specific fields
(e.g. `"clear only the address fields"`); targeted clears go
through the LLM matcher with a delete-only filter.

Optional `form_fields` and `page_range` (alias `pages`) behave
the same as on [Form Fill](api:POST/form/fill).

Synchronous by default — returns the cleared `FormResult`
inline (including a `pdf_url` you can `GET` to download the
PDF binary). Set `async: true` to receive `{job_id, status:
"pending"}` and poll [GET /job/{jobId}](api:GET/job/{jobId}).

Billed at **3 credits per page**. Requires the `form_filler`
feature flag to be enabled for your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.form.clear(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — Direct binary upload of the PDF. Mutually exclusive with `file_url` and `form_id`.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — Public or pre-signed URL of a PDF Pulse will download. Mutually exclusive with `file` and `form_id`.
    
</dd>
</dl>

<dl>
<dd>

**form_id:** `typing.Optional[str]` — Reference to a previously processed form. Mutually exclusive with `file` / `file_url`.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` — Optional natural language description of what to clear. When omitted, Pulse clears everything user-filled deterministically.
    
</dd>
</dl>

<dl>
<dd>

**form_fields:** `typing.Optional[str]` — Optional JSON-encoded array of `FormCell` objects to override detected cells. Multipart bodies must serialise this field as a string.
    
</dd>
</dl>

<dl>
<dd>

**page_range:** `typing.Optional[str]` — Restrict the operation to a subset of pages, e.g. `"1-3,5"`.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[str]` — Set to `"true"` to run asynchronously and receive `{job_id, status}` immediately.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Batch
<details><summary><code>client.batch.<a href="src/pulse/batch/client.py">extract</a>(...) -> BatchExtractResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process multiple files in parallel. Enumerates files from an input
source (S3 prefix, local directory, or URL list), calls
[Extract](api:POST/extract) for each file, and saves results to an
output destination.

Always asynchronous — returns a batch job ID immediately.
Poll [GET /job/{jobId}](api:GET/job/{jobId}) for real-time progress
including per-file completion status.

See the [Extract](api:POST/extract) endpoint for details on
`extract_options` and the [Batch Processing guide](/batch) for
an overview of the batch pipeline.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse, BatchInputSource, BatchOutputDestination
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.batch.extract(
    input=BatchInputSource(),
    output=BatchOutputDestination(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `BatchInputSource` — Source of files to process.
    
</dd>
</dl>

<dl>
<dd>

**output:** `BatchOutputDestination` — Where to save extraction result JSON files.
    
</dd>
</dl>

<dl>
<dd>

**extract_options:** `typing.Optional[typing.Dict[str, typing.Any]]` — Options forwarded to each `/extract` call (e.g. `pages`, `figureProcessing`, `extensions`).
    
</dd>
</dl>

<dl>
<dd>

**workers:** `typing.Optional[int]` — Number of parallel workers. Higher values increase throughput but consume more server resources.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/pulse/batch/client.py">schema</a>(...) -> BatchSchemaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply schema extraction to multiple items in parallel.
Mode is inferred from the input:

**Single mode** — Provide `extraction_ids` or `batch_extract_id`
with `schema_config` to apply one schema to each extraction.

**Split mode** — Provide `split_ids` or `batch_split_id`
with `split_schema_config` to apply per-topic schemas to each split.

Each child call goes through the full [Schema](api:POST/schema) code
path. Poll [GET /job/{jobId}](api:GET/job/{jobId}) for real-time
progress.

See the [Schema](api:POST/schema) endpoint for details on
`schema_config` and `split_schema_config`, and the
[Batch Processing guide](/batch) for an overview of the batch
pipeline.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse, BatchOutputDestination
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.batch.schema(
    output=BatchOutputDestination(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**output:** `BatchOutputDestination` — Where to save schema result JSON files.
    
</dd>
</dl>

<dl>
<dd>

**batch_extract_id:** `typing.Optional[str]` — ID of a prior `/batch/extract` run (single mode).
    
</dd>
</dl>

<dl>
<dd>

**extraction_ids:** `typing.Optional[typing.List[str]]` — Explicit list of extraction IDs (single mode).
    
</dd>
</dl>

<dl>
<dd>

**batch_split_id:** `typing.Optional[str]` — ID of a prior `/batch/split` run (split mode).
    
</dd>
</dl>

<dl>
<dd>

**split_ids:** `typing.Optional[typing.List[str]]` — Explicit list of split IDs (split mode).
    
</dd>
</dl>

<dl>
<dd>

**schema_config:** `typing.Optional[SchemaConfig]` — Schema configuration for single mode. Applied to each extraction.
    
</dd>
</dl>

<dl>
<dd>

**split_schema_config:** `typing.Optional[typing.Dict[str, TopicSchemaConfig]]` — Per-topic schema configurations for split mode. Keys must match the topic names from the splits.
    
</dd>
</dl>

<dl>
<dd>

**page_range:** `typing.Optional[str]` — Page range filter for single mode (e.g. `1-5,10`).
    
</dd>
</dl>

<dl>
<dd>

**workers:** `typing.Optional[int]` — Number of parallel workers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/pulse/batch/client.py">tables</a>(...) -> BatchTablesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extract tables from multiple existing extractions in parallel.
Each child call goes through the full [Tables](api:POST/tables) code
path.

Extractions are identified by either a `batch_extract_id` (from a
prior [Batch Extract](api:POST/batch/extract) run) or an explicit
list of `extraction_ids`.

Poll [GET /job/{jobId}](api:GET/job/{jobId}) for real-time progress.

See the [Tables](api:POST/tables) endpoint for details on
`tables_config` and the [Batch Processing guide](/batch) for an
overview of the batch pipeline.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse, BatchOutputDestination
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.batch.tables(
    output=BatchOutputDestination(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**output:** `BatchOutputDestination` — Where to save table result JSON files.
    
</dd>
</dl>

<dl>
<dd>

**batch_extract_id:** `typing.Optional[str]` — ID of a prior `/batch/extract` run. All completed child extraction IDs will be used.
    
</dd>
</dl>

<dl>
<dd>

**extraction_ids:** `typing.Optional[typing.List[str]]` — Explicit list of extraction IDs to process.
    
</dd>
</dl>

<dl>
<dd>

**tables_config:** `typing.Optional[TablesConfig]` — Table extraction configuration forwarded to each `/tables` call.
    
</dd>
</dl>

<dl>
<dd>

**workers:** `typing.Optional[int]` — Number of parallel workers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/pulse/batch/client.py">split</a>(...) -> BatchSplitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Split multiple existing extractions by topics in parallel.
Each child call goes through the full [Split](api:POST/split) code
path.

Extractions are identified by either a `batch_extract_id` (from a
prior [Batch Extract](api:POST/batch/extract) run) or an explicit
list of `extraction_ids`.

Poll [GET /job/{jobId}](api:GET/job/{jobId}) for real-time progress.

See the [Split](api:POST/split) endpoint for details on
`split_config` and the [Batch Processing guide](/batch) for an
overview of the batch pipeline.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse, BatchOutputDestination, SplitConfig, TopicDefinition
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.batch.split(
    output=BatchOutputDestination(),
    split_config=SplitConfig(
        split_input=[
            TopicDefinition(
                name="name",
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**output:** `BatchOutputDestination` — Where to save split result JSON files.
    
</dd>
</dl>

<dl>
<dd>

**split_config:** `SplitConfig` — Split configuration with topic definitions. Applied to each extraction.
    
</dd>
</dl>

<dl>
<dd>

**batch_extract_id:** `typing.Optional[str]` — ID of a prior `/batch/extract` run. All completed child extraction IDs will be used.
    
</dd>
</dl>

<dl>
<dd>

**extraction_ids:** `typing.Optional[typing.List[str]]` — Explicit list of extraction IDs to process.
    
</dd>
</dl>

<dl>
<dd>

**workers:** `typing.Optional[int]` — Number of parallel workers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pipeline
<details><summary><code>client.pipeline.<a href="src/pulse/pipeline/client.py">execute</a>(...) -> PipelineExecuteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Chain multiple processing steps (extract, schema, split, tables) into a
single request with inline configurations. No saved pipeline required.

The `steps` object defines what to run and in what order. Outputs flow
forward automatically — you never need to pass extraction IDs between
steps.

**Supported step combinations:**
- `extract` — extract a single document
- `extract` → `schema` — extract then apply structured schema
- `extract` → `split` — extract then split into topics
- `extract` → `split` → `schema` — extract, split by topic, apply per-topic schemas
- `extract` → `tables` — extract then extract structured tables
- `batch_extract` → `schema` — extract multiple files, combine into one schema output

**Document input:**
- Single file: provide `fileUrl` in JSON or `file` via multipart
- Multiple files (batch_extract): provide `fileUrls` in JSON or multiple `file` fields via multipart

Set `async: true` to return immediately with a `job_id` for polling via
`GET /job/{jobId}`.

Set `autoDelete: true` for zero-retention mode — all stored artifacts
are deleted immediately after you receive the results. Requires
`save_extractions` to be disabled for your organization.

Requires the `enable_adhoc_pipeline` feature flag.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse, PipelineSteps
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.pipeline.execute(
    steps=PipelineSteps(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**steps:** `PipelineSteps` — Ordered step definitions. Key order determines execution order.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — URL of the document to process. Use with `extract` step.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — If true, returns immediately with a `job_id` for polling via `GET /job/{jobId}`.
    
</dd>
</dl>

<dl>
<dd>

**auto_delete:** `typing.Optional[bool]` — If true, all stored artifacts are deleted immediately after you receive the results. The inline data in the response is unaffected. Requires `save_extractions` to be disabled for your organization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs
<details><summary><code>client.jobs.<a href="src/pulse/jobs/client.py">get_job</a>(...) -> JobStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the status and retrieve results of an asynchronous job
(submitted via any endpoint with `async: true`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.jobs.get_job(
    job_id="jobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — Identifier returned from an async job submission.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/pulse/jobs/client.py">cancel_job</a>(...) -> JobCancellationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attempts to cancel an asynchronous job that is currently pending
or processing. Jobs that have already completed will remain unchanged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.jobs.cancel_job(
    job_id="jobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — Identifier returned from an async job submission.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Results
<details><summary><code>client.results.<a href="src/pulse/results/client.py">get_pdf</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the PDF binary produced by a `/form/detect`,
`/form/fill`, or `/form/clear` job. The `pdf_url` field on a
`FormResult` points at this endpoint — you can hand it
directly to a browser, embed it in an `<iframe>`, or fetch the
bytes from a backend.

Returns `404` for non-form jobs (no PDF was produced) and for
form jobs whose PDF artifact is no longer available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.results.get_pdf(
    job_id="jobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — Job identifier from a form endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.results.<a href="src/pulse/results/client.py">get_image</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream a PNG/JPEG visual image referenced by an extraction
response under `bounding_boxes.Images[].image_url`.

The URL is API-hosted instead of raw S3 — the underlying object
store is intentionally not part of the public contract. The host
in `image_url` mirrors the request origin (e.g. a request to a
beta deployment returns image URLs on that same host).

**Authentication is required.** Unlike the legacy single-use
`/large_results/{jobId}` route, visual artifacts are
independently-addressable resources — every fetch must present a
valid API key for the owning org. There is no anonymous /
TTL-based fallback. Use the same `x-api-key` header you use for
`/extract`.

Fetching an image does **not** consume the parent extraction's
result-delivery slot, so one extraction can produce many image
URLs and each can be fetched repeatedly while the artifact is
retained.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.results.get_image(
    job_id="jobId",
    filename="filename",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — Job identifier — same value used in the `image_url` returned from `/extract`.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` — Visual filename — e.g. `excel_image_1_1.png`. Must be the exact `filename` segment from the `image_url`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LargeResults
<details><summary><code>client.large_results.<a href="src/pulse/large_results/client.py">get_large_result</a>(...) -> ExtractResultCore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the full result for a large extraction. When `/extract`
or `GET /job/{jobId}` returns `is_url: true`, fetch the complete
result from the URL provided.  The URL is single-use: after a
successful download the resource is deleted and subsequent
requests return 410 Gone.

For form jobs (`/form/detect`, `/form/fill`, `/form/clear`)
you don't need this endpoint at all — `GET /job/{jobId}`
already returns the full `FormResult` inline under `result`,
and the `pdf_url` field points at
[GET /results/{jobId}/pdf](api:GET/results/{jobId}/pdf) for the
binary.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.large_results.get_large_result(
    job_id="jobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — Job identifier from the extraction response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/pulse/webhooks/client.py">create_webhook_link</a>() -> CreateWebhookLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a temporary link to the Svix webhook portal where users can manage their webhook endpoints and view message logs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pulse import Pulse
from pulse.environment import PulseEnvironment

client = Pulse(
    api_key="<value>",
    environment=PulseEnvironment.DEFAULT,
)

client.webhooks.create_webhook_link()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

