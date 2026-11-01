from model.Produto import Produto

def principal():
    p = Produto("Caneta", 100, 20, 200)
    p.vender(95)
    p.vender(10)
    p.comprar(150)
    p.comprar(100)
    p.comprar(40)
    p.vender(1)
    print(p.getQtdeEstoque())
    p.exibirHistorico()

if __name__ == "__name__":
    principal()