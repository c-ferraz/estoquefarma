//  var botao = document.getElementById("buconteudoon1");
//  botao.addEventListener('click', function() {
//                                      login();
//                                  });
// function ValidarAcesso(){
// var nome="useradm";
// var senha="123456";
// var ninput=document.getElementById("input1");
// var sinput=document.getElementById("input2");
// if (nome === ninput && senha === sinput){
    

// }


// }

var usuarios = [
    {"login": "useradm", "senha": "123456"},
    {"login": "test", "senha": "test"},
    {"login": "estoquefarma", "senha": "estoquefarma"},
];

function login() {
    var usuario = document.getElementsByName('usuario')[0].value.toLowerCase();
    var senha = document.getElementsByName('senha')[0].value;
    

    for (var u in usuarios) {
        var us = usuarios[u];
        if (us.login === usuario && us.senha === senha) {
            window.location = "inicial.html";
            return true;
        }
    }
        
    alert("Dados incorretos, tente novamente.");
    window.location = "index.html";
    return false;
        
}

function cadastrar(){
    const conteudo = document.getElementById("conteudo");
    conteudo.style.display='block';
    conteudo.innerHTML=`
    <form action="cadastrar_produto" method="POST">
    <input type='hidden' id="csrfmiddlewaretoken" name='csrfmiddlewaretoken' value=""/>
    <div class="inputCadastro" id="">
    <label>Nome do Produto: </label>
    <input type="text"  name="nomeProduto"/>
    </div>
    <div class="inputCadastro">
    <label>Codigo de Barra: </label>
    <input type="number"   name="codBarraProduto"/>
    </div>
    <div class="inputCadastro">
    <label>Lote: </label>
    <input type="number"   name="loteProduto"/>
    </div>
    <div class="inputCadastro">
    <a href="inicial.html"><input type="submit" value="Cadastrar"/></a>
    </div>
    </form>
    `;
    document.getElementById("csrfmiddlewaretoken").value = csrftoken;
    
    
}


function alocar(){
    const conteudo = document.getElementById("conteudo");
    conteudo.style.display='block';
    conteudo.innerHTML=`<form action="" method="POST">
    <div class="inputCadastro" id="">
    <label>Codigo de Barra: </label>
    <input type="text"  name="nomeProduto"/>
    </div>
    <div class="inputCadastro">
    <label>Local: </label>
    <input type="number"   name="codBarraProduto"/>
    </div>
    <div class="inputCadastro">
<label>Quantidade: </label>
<input type="number"   name="loteProduto"/>
</div>
    <div class="inputCadastro">
<label>Validade: </label>
<input type="number"   name="loteProduto"/>
</div>
<div class="inputCadastro">
<a href="inicial.html"><button type="button" >Alocar</button></a>
</div>
</form>
`;
}
function desalocar(){
    const conteudo = document.getElementById("conteudo");
    conteudo.style.display='block';
    conteudo.innerHTML=`<form action="" method="POST">
    <div class="inputCadastro" id="">
    <label>Codigo de Barra: </label>
    <input type="text"  name="nomeProduto"/>
    </div>
    <div class="inputCadastro">
    <label>Local: </label>
    <input type="number"   name="codBarraProduto"/>
   </div>
   <div class="inputCadastro">
<a href="inicial.html"><button type="button" >Desalocar</button></a>
</div>
</form>
`;
}

/* #conteudo{
  background-color: chartreuse;
  width: 500px;
  height: 700px;mn,
} */