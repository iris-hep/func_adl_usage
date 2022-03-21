# func_adl_usage

 A Jupyter Book as a user's manual for ServiceX

## Usage

This book is published [here]()

## Development

Feel free to submit pull requests with new demos or ideas and feel free to also submit issues with ideas of what should be in here.

The code and markdown is based `jupyter-book`, which is described in lots of detail on [jupyterbook.org](https://jupyterbook.org). Its manual has a huge number of examples of the types of things you can do in their [`rst` version of markdown](https://jupyterbook.org/content/myst.html).

### Setting up your environment

```bash
pip install -r requirements.txt
```

Make sure you have a `servicex.yaml` file somewhere that the backends will find it, with a `xaod` and `uproot` backends defined, depending on what you want to publish.

### Building and Publishing

The model used to develop the book is to directly publish the notebooks as-is. `jupyter-book`. This means once you have a notebook page working, you should restart the server and run all cells.

To build the book use the following command. It will not actually run the notebooks, just build the web pages:

```bash
jupyter-book build --all user_manual
```

And then to push the pages for web publication:

```bash
ghp-import -n -p -f ./book/_build/html
```

GitHub takes a few minutes to update is pages. If the table of contents changes you'll need to refresh your browser if you are looking at an old page.
