const express = require('express');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const path = require('path');
// Serve arquivos estáticos (index.html, style.css, script.js, etc.)
app.use(express.static(path.join(__dirname)));
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/portfolio', async (req, res) => {
  const body = {
    name: req.body.name,
    email: req.body.email,
    description: req.body.description,
    number: req.body.number
  };

  function verificarDados() {
    try {
      if (Object.values(body).every(val => String(val).trim().length > 0)) {
        return true;
      } else {
        return false;
      }
    } catch (dataerror) {
      console.log({ message: "Erro na integridade dos dados..." });
      return body;
    }
  }

  async function validateName(name) {
    if (/^[A-Za-z\s]+$/.test(name)) {
      return true;
    } else {
      return false;
    }
  }

  async function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(email)) {
      return true;
    } else if ((email.match(/@/g) || []).length === 1 && (email.match(/\./g) || []).length >= 1) {
      return true;
    } else {
      return false;
    }
  }

  async function validateDescription(description) {
    if (typeof description === 'string' && description.length > 0) {
      return true;
    } else {
      return false;
    }
  }

  async function validateNumber(number) {
    if (!isNaN(number) && String(number).trim() !== "") {
      return true;
    } else {
      return false;
    }
  }

  async function callfunctions() {
    try {
      const vName = await validateName(body.name);
      const vEmail = await validateEmail(body.email);
      const vDesc = await validateDescription(body.description);
      const vNum = await validateNumber(body.number);

      if (vName && vEmail && vDesc && vNum) {
        return res.status(201).json({ message: "Dados recebidos" });
      } else {
        return res.status(400).json({ message: "ERRO" });
      }
    } catch (internalError) {
      return res.status(500).json({
        message: "ERRO; Falha interna em nosso serviço, aguarde um momento.."
      });
    }
  }

  await callfunctions();
});

app.listen(3000, () => {
  console.log("Servidor rodando: PORTA 3000");
});
