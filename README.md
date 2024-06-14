# Prova2-Modulo10
O objetivo desse repositório é a entrega da parte prática realizada na Prova 2 do Módulo 10, onde o objetivo era transformar um código Flask em FastAPI e adicionar um sistema de logs juntamente com NGINX e Docker compose.

[Screencast from 14-06-2024 10:40:31.webm](https://github.com/joaocarazzato/Prova2-Modulo10/assets/99187756/5278ce9b-6a56-495a-8e71-aea6ca555e3d)

## Como executar?

Para executar é muito simples, você simplesmente precisa ir na pasta inicial da nossa aplicação e digitar

```
docker compose up --build
```

Assim, toda a aplicação será levantada de uma só vez, já tendo seus logs mapeados do docker compose para seu diretório raiz, para que seja possível armazená-los e vê-los no momento que quiser.

Para acessar a aplicação é só ir até a rota **http://localhost:8000**, e caso queira acessar as rotas de blog, é só ir até a rota **http://localhost:8000/blog** e explorar as rotas(como a de criação de um blog post, sendo o endereço **http://localhost:8000/blog/blog** onde é uma requisição **POST**).

Além disso, caso queira testar nossa aplicação, temos uma documentação de todas as rotas na pasta **docs** dentro do arquivo **Insomnia_2024-06-14.yaml**. Só é necessário importá-lo ao Insomnia e testar as rotas.