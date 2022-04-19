# pylanceのvscodeでのセッティング

```{.json}
"python.languageServer": "Pylance",
```

```{.json}
"python.analysis.typeCheckingMode": "strict",
```

- サードパッケージの場所を登録する．

```{.json}
"python.autoComplete.extraPaths": [
        "./.venv/lib/python3.10/site-packages/"
    ],
```
