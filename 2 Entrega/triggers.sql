-- Atualiza o estoque removendo os intens da venda
CREATE TRIGGER trg_atualiza_estoque_venda AFTER 
	INSERT ON venda_produto
    FOR EACH ROW
	EXECUTE PROCEDURE fnct_atualiza_estoque_venda();

-- Atualiza o estoque adcionando os intens da compra
CREATE TRIGGER trg_atualiza_estoque_compra AFTER
    INSERT ON compra_produto
    FOR EACH ROW
	EXECUTE PROCEDURE fnct_atualiza_estoque_compra();
