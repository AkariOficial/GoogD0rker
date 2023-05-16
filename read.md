## GoogD0rker

### Sobre
> GoogD0rker é uma ferramenta para disparar google dorks contra um domínio de destino, é puramente para OSINT contra um domínio de destino específico. Isso produzirá todos os resultados do Google para cada uma das tarefas, para que você possa encontrar uma vulnerabilidade. Um erro 503 significa que você precisa de um novo IP, pois o Google sabe que você está tramando algo! Isso enviará os resultados para os arquivos e você poderá navegar e ver o que encontrou.

### requisitos basicos
 - ubuntu 18 ou superior
 - python 3.10 ou superior
 - pyenv necessário!

-----

### instale o git se n tiver:
```bash
 apt update && apt install -y git
```

### instale o pyenv:
```bash
 sudo apt-get update && sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python2-dev python3-dev aria2 && curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash && touch .bashrc && echo '
export PYTHON_BUILD_ARIA2_OPTS="-x 10 -k 1M"
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
' >> .bashrc && source .bashrc && pyenv update && pyenv --version
```

### instale uma versão do python com pyenv:
```bash
 pyenv install 3.10.5 && pyenv global 3.10.5
```

### clone o repositório:
```bash
 git clone https://github.com/ZephrFish/GoogD0rker $HOME/GoogleDorker && cd $HOME/GoogleDorker && clear && ls
```

### instale as dependências necessárias:
```bash
 pip install -r requirements.txt
```

### e por fim, rode o programa:
```bash
 python googD0rk-donotuse.py -d example.com
```
