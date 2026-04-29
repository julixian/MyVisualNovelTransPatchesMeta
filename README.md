# MyVisualNovelTranslPatch

Static update manifests for visual novel translation patches.

Files are grouped by engine and named by patch project id:

```text
<Engine>/<ProjectName>.json
```

Each manifest uses this shape:

```json
{
  "project": "DimensionToTsuLovers_cn",
  "latest_version": "1.5.0",
  "release_url": "https://github.com/julixian/MyVisualNovelTranslPatch",
  "message": "No newer patch is currently available."
}
```

`latest_version` must be a strict semantic version: `major.minor.patch`.
