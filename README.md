# ILDL
Shared repository of Innan Lab. for Deep Learning

## installation

1. Install [Homebrew](http://brew.sh/)

1. Install git and [pyenv](https://github.com/yyuu/pyenv) via Homebrew:
   `brew install git pyenv`

1. Install [Anaconda](https://docs.continuum.io/) or Miniconda via pyenv:

    ```sh
    pyenv install anaconda
    pyenv install anaconda3-4.1.1
    pyenv global anaconda3-4.1.1
    pyenv versions
    ```
1. Setup [`~/.gitconfig`](https://git-scm.com/book/ja/v1/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-%E6%9C%80%E5%88%9D%E3%81%AEGit%E3%81%AE%E6%A7%8B%E6%88%90)
   and [SSH key](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
   for your GitHub account

1. Clone this repository to your local machine:

    ```
    mkdir ~/git
    cd ~/git
    git clone git@github.com:heavywatal/ildl.git
    cd ildl/
    git submodule update --init
    ```
