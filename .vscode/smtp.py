import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_body_email():
    html_content = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Marketing</title>
    <style>
        body { margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4; }
        .container { width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; }
        .header { background-color: #007bff; color: #ffffff; padding: 20px; text-align: center; }
        .content { padding: 30px; line-height: 1.6; color: #333333; }
        .button-container { text-align: center; padding: 20px; }
        .button { background-color: #28a745; color: #ffffff; padding: 15px 25px; text-decoration: none; border-radius: 5px; font-weight: bold; }
        .footer { background-color: #eeeeee; color: #777777; padding: 20px; text-align: center; font-size: 12px; }
    </style>
</head>
<body>
    <table role="presentation" class="container" cellspacing="0" cellpadding="0" border="0">
        <tr>
            <td class="header">
                <h1>Título do Seu E-mail</h1>
            </td>
        </tr>
        <tr>
            <td class="content">
                <h2>Olá, [Nome]!</h2>
                <p>Esta é uma estrutura básica de e-mail marketing pronta para ser utilizada. O design é focado em legibilidade e compatibilidade.</p>
                <p>Você pode adicionar imagens, mudar as cores e ajustar o texto conforme sua necessidade.</p>
            </td>
        </tr>
        <tr>
            <td class="button-container">
                <a href="https://seusite.com" class="button">Clique Aqui Agora</a>
            </td>
        </tr>
        <tr>
            <td class="footer">
                <p>&copy; 2024 Sua Empresa. Todos os direitos reservados.</p>
                <p><a href="#">Descadastrar-se</a></p>
            </td>
        </tr>
    </table>
</body>
</html>"""
    return html_content

def get_credentials():
    return {
        "remetente": "klebersantanadeoliveira07@gmail.com",
        "destinatario": "kleberdevion@gmail.com",
        "senha": "yssn ywxs mrtk fpzw"
    }

def send_email():
    credentials = get_credentials()
    html_body = get_body_email()
    
    msg = MIMEMultipart()
    msg['From'] = credentials['remetente']
    msg['To'] = credentials['destinatario']
    msg['Subject'] = "Email Marketing"
    
    msg.attach(MIMEText(html_body, 'html'))
    
    try:
        # O PoolScript mencionou porta 467, mas o padrão SSL do Gmail é 465
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(credentials['remetente'], credentials['senha'])
        server.send_message(msg)
        server.quit()
        return {"status": 200, "message": "Email enviado com sucesso"}
    except Exception as e:
        return {"status": 404, "message": str(e)}

if __name__ == "__main__":
    result = send_email()
    print(result)