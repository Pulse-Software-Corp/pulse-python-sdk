# Reference
<details><summary><code>client.<a href="src/pulse/client.py">extract</a>(...) -> AsyncHttpResponse[ExtractResponse]</code></summary>
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
client.extract(
    file_url="fileUrl",
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

**file_url:** `str` — Public or pre-signed URL that Pulse will download and extract.
    
</dd>
</dl>

<dl>
<dd>

**structured_output:** `typing.Optional[ExtractJsonInputStructuredOutput]` — Recommended method for schema-guided extraction. Contains the schema and optional prompt in a single object.
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[ExtractJsonInputSchema]` — (Deprecated) JSON schema describing structured data to extract. Use structuredOutput instead. Accepts either a JSON object or a stringified JSON representation.
    
</dd>
</dl>

<dl>
<dd>

**experimental_schema:** `typing.Optional[ExtractJsonInputExperimentalSchema]` — (Deprecated) Experimental schema definition used for feature flagged behaviour. Accepts either a JSON object or a stringified JSON representation.
    
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

**return_html:** `typing.Optional[bool]` — Whether to include HTML representation alongside markdown in the response.
    
</dd>
</dl>

<dl>
<dd>

**thinking:** `typing.Optional[bool]` — (Deprecated) Enables expanded rationale output for debugging.
    
</dd>
</dl>

<dl>
<dd>

**storage:** `typing.Optional[ExtractJsonInputStorage]` — Options for persisting extraction artifacts. When enabled (default), artifacts are saved to storage and a database record is created.
    
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

<details><summary><code>client.<a href="src/pulse/client.py">extract_async</a>(...) -> AsyncHttpResponse[ExtractAsyncResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
client.extract_async(
    file_url="fileUrl",
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

**file_url:** `str` — Public or pre-signed URL that Pulse will download and extract.
    
</dd>
</dl>

<dl>
<dd>

**structured_output:** `typing.Optional[ExtractJsonInputStructuredOutput]` — Recommended method for schema-guided extraction. Contains the schema and optional prompt in a single object.
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[ExtractJsonInputSchema]` — (Deprecated) JSON schema describing structured data to extract. Use structuredOutput instead. Accepts either a JSON object or a stringified JSON representation.
    
</dd>
</dl>

<dl>
<dd>

**experimental_schema:** `typing.Optional[ExtractJsonInputExperimentalSchema]` — (Deprecated) Experimental schema definition used for feature flagged behaviour. Accepts either a JSON object or a stringified JSON representation.
    
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

**return_html:** `typing.Optional[bool]` — Whether to include HTML representation alongside markdown in the response.
    
</dd>
</dl>

<dl>
<dd>

**thinking:** `typing.Optional[bool]` — (Deprecated) Enables expanded rationale output for debugging.
    
</dd>
</dl>

<dl>
<dd>

**storage:** `typing.Optional[ExtractJsonInputStorage]` — Options for persisting extraction artifacts. When enabled (default), artifacts are saved to storage and a database record is created.
    
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
<details><summary><code>client.jobs.<a href="src/pulse/jobs/client.py">get_job</a>(...) -> AsyncHttpResponse[JobStatusResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the status and retrieve results of an asynchronous job
(e.g., submitted via `/extract_async`).
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

**job_id:** `str` — Identifier returned from an async job submission (e.g., `/extract_async`).
    
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

<details><summary><code>client.jobs.<a href="src/pulse/jobs/client.py">cancel_job</a>(...) -> AsyncHttpResponse[JobCancellationResponse]</code></summary>
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

**job_id:** `str` — Identifier returned from an async job submission (e.g., `/extract_async`).
    
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
<details><summary><code>client.webhooks.<a href="src/pulse/webhooks/client.py">create_webhook_link</a>() -> AsyncHttpResponse[CreateWebhookLinkResponse]</code></summary>
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

