-- Verifica se o vendedor cumpriu a meta mensal parametrizada em seu perfil
CREATE OR REPLACE FUNCTION verifica_meta_vendedor (cpf_vendedor IN NUMBER, data_meta IN NUMBER)
    RETURN VARCHAR
IS
    meta_atingida VARCHAR(20);
    meta_vendedor NUMBER;
    valor_vendas NUMBER;
BEGIN
    SELECT meta INTO meta_vendedor
    FROM vendedor
    WHERE vendedor.cpf = cpf_vendedor;
    
    SELECT SUM(valor_total) INTO valor_vendas
    FROM venda
    WHERE venda.cpf_funcionario_venda = cpf_vendedor
    AND TO_CHAR(venda.data_venda,'MM/YY') = data_meta;
    
    IF valor_vendas >= meta_vendedor THEN
        meta_atingida := 'Meta atingida';
    ELSE
        meta_atingida := 'Meta não atingida';
    END IF;
END;
