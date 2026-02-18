# Reference
<details><summary><code>client.<a href="src/pulse/client.py">extract</a>(...) -&gt; AsyncHttpResponse[ExtractResponse]</code></summary>
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

**Note:** Both sync and async modes return HTTP 200. When `async` is true
the response body contains `{ job_id, status }` instead of the full
extraction result.
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

client = Pulse(
    api_key="YOUR_API_KEY",
)
client.extract()

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

**file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — Public or pre-signed URL that Pulse will download and extract. Required unless file is provided.
    
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

**experimental_schema:** `typing.Optional[ExtractRequestExperimentalSchema]` — (Deprecated) Experimental schema definition used for feature flagged behaviour. Accepts either a JSON object or a stringified JSON representation.
    
</dd>
</dl>

<dl>
<dd>

**schema_prompt:** `typing.Optional[str]` — (Deprecated) Natural language prompt for schema-guided extraction. Use structuredOutput.schemaPrompt instead.
    
</dd>
</dl>

<dl>
<dd>

**custom_prompt:** `typing.Optional[str]` — (Deprecated) Custom instructions that augment the default extraction behaviour.
    
</dd>
</dl>

<dl>
<dd>

**chunking:** `typing.Optional[str]` — Comma-separated list of chunking strategies to apply (for example `semantic,header,page,recursive`).
    
</dd>
</dl>

<dl>
<dd>

**chunk_size:** `typing.Optional[int]` — Override for maximum characters per chunk when chunking is enabled.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Page range filter supporting segments such as `1-2` or mixed ranges like `1-2,5`.
    
</dd>
</dl>

<dl>
<dd>

**extract_figure:** `typing.Optional[bool]` — Toggle to enable figure extraction in results.
    
</dd>
</dl>

<dl>
<dd>

**figure_description:** `typing.Optional[bool]` — Toggle to generate descriptive captions for extracted figures.
    
</dd>
</dl>

<dl>
<dd>

**show_images:** `typing.Optional[bool]` — Embed base64-encoded images inline in figure tags in the output. Increases response size.
    
</dd>
</dl>

<dl>
<dd>

**return_html:** `typing.Optional[bool]` — Whether to include HTML representation alongside markdown in the response.
    
</dd>
</dl>

<dl>
<dd>

**effort:** `typing.Optional[bool]` — Enable extended reasoning mode for higher quality extraction on complex documents. Uses a more powerful model at higher latency.
    
</dd>
</dl>

<dl>
<dd>

**thinking:** `typing.Optional[bool]` — (Deprecated) Enables expanded rationale output for debugging.
    
</dd>
</dl>

<dl>
<dd>

**storage:** `typing.Optional[ExtractRequestStorage]` — Options for persisting extraction artifacts. When enabled (default), artifacts are saved to storage and a database record is created.
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` — If true, returns immediately with a job_id for polling via GET /job/{jobId}. Otherwise processes synchronously.
    
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

<details><summary><code>client.<a href="src/pulse/client.py">extract_async</a>(...) -&gt; AsyncHttpResponse[AsyncSubmissionResponse]</code></summary>
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

client = Pulse(
    api_key="YOUR_API_KEY",
)
client.extract_async()

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

**file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — Public or pre-signed URL that Pulse will download and extract. Required unless file is provided.
    
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

**experimental_schema:** `typing.Optional[ExtractAsyncRequestExperimentalSchema]` — (Deprecated) Experimental schema definition used for feature flagged behaviour. Accepts either a JSON object or a stringified JSON representation.
    
</dd>
</dl>

<dl>
<dd>

**schema_prompt:** `typing.Optional[str]` — (Deprecated) Natural language prompt for schema-guided extraction. Use structuredOutput.schemaPrompt instead.
    
</dd>
</dl>

<dl>
<dd>

**custom_prompt:** `typing.Optional[str]` — (Deprecated) Custom instructions that augment the default extraction behaviour.
    
</dd>
</dl>

<dl>
<dd>

**chunking:** `typing.Optional[str]` — Comma-separated list of chunking strategies to apply (for example `semantic,header,page,recursive`).
    
</dd>
</dl>

<dl>
<dd>

**chunk_size:** `typing.Optional[int]` — Override for maximum characters per chunk when chunking is enabled.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Page range filter supporting segments such as `1-2` or mixed ranges like `1-2,5`.
    
</dd>
</dl>

<dl>
<dd>

**extract_figure:** `typing.Optional[bool]` — Toggle to enable figure extraction in results.
    
</dd>
</dl>

<dl>
<dd>

**figure_description:** `typing.Optional[bool]` — Toggle to generate descriptive captions for extracted figures.
    
</dd>
</dl>

<dl>
<dd>

**show_images:** `typing.Optional[bool]` — Embed base64-encoded images inline in figure tags in the output. Increases response size.
    
</dd>
</dl>

<dl>
<dd>

**return_html:** `typing.Optional[bool]` — Whether to include HTML representation alongside markdown in the response.
    
</dd>
</dl>

<dl>
<dd>

**effort:** `typing.Optional[bool]` — Enable extended reasoning mode for higher quality extraction on complex documents. Uses a more powerful model at higher latency.
    
</dd>
</dl>

<dl>
<dd>

**thinking:** `typing.Optional[bool]` — (Deprecated) Enables expanded rationale output for debugging.
    
</dd>
</dl>

<dl>
<dd>

**storage:** `typing.Optional[ExtractAsyncRequestStorage]` — Options for persisting extraction artifacts. When enabled (default), artifacts are saved to storage and a database record is created.
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` — If true, returns immediately with a job_id for polling via GET /job/{jobId}. Otherwise processes synchronously.
    
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

<details><summary><code>client.<a href="src/pulse/client.py">split</a>(...) -&gt; AsyncHttpResponse[SplitResponse]</code></summary>
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

client = Pulse(
    api_key="YOUR_API_KEY",
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

**async_:** `typing.Optional[bool]` — If true, returns immediately with a job_id for polling via  GET /job/{jobId}. Otherwise processes synchronously.
    
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

<details><summary><code>client.<a href="src/pulse/client.py">schema</a>(...) -&gt; AsyncHttpResponse[SchemaResponse]</code></summary>
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

**Split mode** — Provide `split_id` + `split_schema_config` to apply
different schemas to different page groups from a prior `/split` call.
Each topic can have its own schema, prompt, and effort setting.

Creates a versioned schema record that can be retrieved later.
Set `async: true` to return immediately with a job_id for polling.
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

client = Pulse(
    api_key="YOUR_API_KEY",
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

**extraction_id:** `typing.Optional[str]` — ID of saved extraction to apply the schema to. Use for single-mode schema extraction.
    
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

**async_:** `typing.Optional[bool]` — If true, returns immediately with a job_id for polling via  GET /job/{jobId}. Otherwise processes synchronously.
    
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
<details><summary><code>client.jobs.<a href="src/pulse/jobs/client.py">get_job</a>(...) -&gt; AsyncHttpResponse[JobStatusResponse]</code></summary>
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

client = Pulse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.jobs.<a href="src/pulse/jobs/client.py">cancel_job</a>(...) -&gt; AsyncHttpResponse[JobCancellationResponse]</code></summary>
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

client = Pulse(
    api_key="YOUR_API_KEY",
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

## Webhooks
<details><summary><code>client.webhooks.<a href="src/pulse/webhooks/client.py">create_webhook_link</a>() -&gt; AsyncHttpResponse[CreateWebhookLinkResponse]</code></summary>
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

client = Pulse(
    api_key="YOUR_API_KEY",
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

