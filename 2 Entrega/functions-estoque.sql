-- Atualiza o estoque removendo os intens da venda
CREATE OR REPLACE FUNCTION fnct_atualiza_estoque_venda()
	RETURNS TRIGGER AS $$
DECLARE
    n INTEGER;
BEGIN
    SELECT p.qtd_estoque INTO n
    FROM produto p
    WHERE p.id_produto = old.id_produto_produto;
    
    UPDATE produto
    SET qtd_estoque = n - new.quantidade
    WHERE id_produto = old.id_produto_produto;
    
    RETURN true
END;
$$ LANGUAGE plpgsql;

-- Atualiza o estoque adcionando os intens da compra
CREATE OR REPLACE FUNCTION fnct_atualiza_estoque_compra()
	RETURNS TRIGGER AS $$
DECLARE
    n INTEGER;
BEGIN
    SELECT p.qtd_estoque INTO n
    FROM produto p
    WHERE p.id_produto = old.id_produto_produto;
	
    UPDATE produto
    SET qtd_estoque = n + new.quantidade
    WHERE id_produto = old.id_produto_produto;
    
    RETURN true
END;
$$ LANGUAGE plpgsql;
