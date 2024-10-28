# mx-strmlit-1
Testing out streamlit here


# Repo Details 

Original work is being done here
https://gitlab.com/fetisfetis/uv-streamlit-1/ 

## Deployed to streamlit cloud 


https://hkzczxowruphdhbkoabnzq.streamlit.app/ 

## NOte changes 

When using UV for the work , when deployed to steramlit you need to make some changes . This is he example 

```js
[project]
name = "StreamLitPanty"
version = "0.1.0"
description = "StreamLitTesting"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "matplotlib>=3.9.2",
    "pandas>=2.2.3",
    "rich>=13.9.3",
    "streamlit>=1.39.0",
]

[tool.poetry]
name = "StreamLitPanty"
version = "0.1.0"
description = "StreamLitTesting"
authors = ["BootyDance <buty@buty>"]  # Replace with your name and email

[tool.poetry.dependencies]
python = ">=3.12"
matplotlib = ">=3.9.2"
pandas = ">=2.2.3"
rich = ">=13.9.3"
streamlit = ">=1.39.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

- Note you added the petry sections , now it gets deployed easily to streamlit cloud
