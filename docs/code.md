Regardless of what your project scope is, you will need to write code. Importantly, the code is therefore a critical
part of your project. This section will provide you with some guidance on how to manage your code development during
your project. In the end of your project, I would expect you to hand in your code together with your thesis:

1. Assuming your code is hosted on a version control system (e.g., Git) and that the code is open-source, you can
    just provide a link to the repository in the preface of your thesis.
2. If your code is not open-source (common in industry projects), you can provide the code as a zip file together with
    your thesis.
3. If you are under a strict NDA, you should not provide the code at all.


## 🔄 Version control

> Code not tracked by version control is code that does not exist.

Yeah, I know that is technically not true, but it is a good rule of thumb. Version control is such a critical part of
code development that it is hard to overstate its importance. Version control allows you to track changes to your code
over time, collaborate with others and manage different versions of your code. There are many version control systems
available, but the most popular one is [Git](https://en.wikipedia.org/wiki/Git). For hosting your code, you can either
use [Github](https://github.com/) or DTU computes [Gitlab](https://lab.compute.dtu.dk) instance.

If you do not know how to use Git (or are new to Git), here are some resources to get you started:

* [Pro Git book](https://git-scm.com/book/en/v2)

* [Git Tutorial for Beginners in 1 hour](https://www.youtube.com/watch?v=8JJ101D3knE)

## 📦 Dependencies

Regardless of what programming language you are using, you will most likely need to use some libraries or packages that
are not part of the standard library. These dependencies are critical to your project, and you need to manage them
properly. How you manage dependencies depends on the programming language you are using.

!!! example "Python"

    In Python anno 2025 that are two main ways to manage and document your dependencies. Either you use
    [pip](https://github.com/pypa/pip) together with a `requirements.txt` file or you use
    [uv](https://docs.astral.sh/uv/) together with a `pyproject.toml` file. Yes, there are other ways to manage
    dependencies in Python, but these are the ways I would recommend.

    As a example, we consider the case where we need to use `pandas` and `scikit-learn` in our project.

    === "pip + requirements.txt"

        Run the following command to install the dependencies:

        ```bash
        pip install pandas scikit-learn
        pip freeze > requirements.txt
        ```

        This will create a `requirements.txt` file that looks like this:

        ```plaintext
        pandas==1.3.3
        scikit-learn==1.0
        ```

    === "uv + pyproject.toml"

        Run the following command to install the dependencies:

        ```bash
        uv init
        uv add pandas scikit-learn
        ```

        This will create a `pyproject.toml` file that contains the dependencies:

        ```toml
        dependencies = [
            "pandas",
            "scikit-learn"
        ]
        ```

## 📝 Code documentation

> Undocumented code is code that does not run.

Again, not technically true, but you get the point. Code documentation is critical to ensure that your code is usable by
others (or your future self). There are many ways to document your code, but the most common way is to use a
`README.md` file in the root of your project. This file should contain information about how to install and run your
code. An example

!!! example

    ```markdown
    # My awesome project
    To run this project, you need to have Python X.Y or later installed. You can install the dependencies
    by running

    `pip install -r requirements.txt`

    To run the main experiments you can run the following command:

    `python main.py`

    afterwards to generate the plots you can run the following command:

    `python plot.py`

    ```

In addition to the `README.md` file, you should preferably also document your code using appropriate comments. The
comments should explain what the code does, not how it does it. A good example is just adding docstrings to your
functions/classes describing what they do.

## Hardware

As any other DTU student you have access to the HPC cluster at DTU. You have hopefully already been introduced and
used it in one of your courses. If not, you can find more information about the cluster on the
[DTU HPC website](https://www.hpc.dtu.dk/). In particular here are some useful links:

* Getting started with ML/AI: <https://www.hpc.dtu.dk/?page_id=4788>
* GPU nodes overview: <https://www.hpc.dtu.dk/?page_id=2129>

!!! note "Space on the HPC cluster"

    The most common limitation you will run into at the HPC cluster is the space limitation. You by default have 30GB
    of space in your home directory. See this [page](https://www.hpc.dtu.dk/?page_id=927) for info on how to check
    your space usage. If you need more space you can write to <support@hpc.dtu.dk> to get some space on the scratch
    filesystem (about 300GB is usually given).

If you are collaborating with a company, you might also have access to their hardware. Ask your external supervisor if
you are not sure.
