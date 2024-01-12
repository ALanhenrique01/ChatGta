import flet as ft

def main(pagina):
    texto = ft.Text("ChatGta")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Digite seu nome")

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"   
        campo_mensagem.value = ""
        pagina.pubsub.send_all(texto_campo_mensagem)

        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem",
                                   on_submit=enviar_mensagem)

    botao_enviar = ft.ElevatedButton("Enviar",
                                      on_click=enviar_mensagem)
    
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        
        pagina.pubsub.send_all(texto)
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem Vindo ao ChatGta!",
                       color="green100",
                         italic=True),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar",
                                    on_click=entrar_chat)]
    )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar Chat",
                                       on_click=iniciar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)
#ft.app(main)
