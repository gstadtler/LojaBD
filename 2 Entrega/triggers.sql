-- Atualiza o estoque removendo os intens da venda
CREATE OR REPLACE TRIGGER trg_atualiza_estoque_venda AFTER
    INSERT ON venda_produto
    FOR EACH ROW
DECLARE
    n PLS_INTEGER;
BEGIN
    SELECT
        p.qtd_estoque
    INTO n
    FROM
        produto p
    WHERE
        p.id_produto = :old.id_produto_produto;

    IF n > 0 THEN
        UPDATE produto
        SET
            qtd_estoque = n - :new.quantidade
        WHERE
            id_produto = :old.id_produto_produto;

    ELSE
        dbms_output.put_line('INSERÇÃO DE REGISTRO CANCELADA, ESTOQUE ZERADO');
        ROLLBACK;
    END IF;

END;

-- Atualiza o estoque adcionando os intens da compra
CREATE OR REPLACE TRIGGER trg_atualiza_estoque_compra AFTER
    INSERT ON compra_produto
    FOR EACH ROW
DECLARE
    n PLS_INTEGER;
BEGIN
    SELECT
        p.qtd_estoque
    INTO n
    FROM
        produto p
    WHERE
        p.id_produto = :old.id_produto_produto;

    UPDATE produto
    SET
        qtd_estoque = n + :new.quantidade
    WHERE
        id_produto = :old.id_produto_produto;

END;