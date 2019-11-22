CREATE OR REPLACE FUNCTION verifica_meta_vendedor (IN cpf_vendedor BIGINT, IN mes INTEGER, IN ano INTEGER)
    RETURNS VARCHAR AS $$
DECLARE
    resultado_meta VARCHAR(20);
    meta_vendedor INTEGER;
    valor_vendas INTEGER;
BEGIN
    SELECT meta INTO meta_vendedor
    FROM vendedor
    WHERE vendedor.cpf = cpf_vendedor;
    
    SELECT SUM(valor_total) INTO valor_vendas
    FROM venda
    WHERE venda.cpf_funcionario_venda = cpf_vendedor
    AND CAST((extract(month from venda.data_venda)) AS INTEGER) = mes
	AND CAST((extract(year from venda.data_venda)) AS INTEGER) = ano;
    
    IF valor_vendas >= meta_vendedor THEN
        resultado_meta := 'Meta atingida';
    ELSE
        resultado_meta := 'Meta não atingida';
    END IF;
	RETURN resultado_meta;
END;
$$ LANGUAGE plpgsql;

-- TESTANDO A FUNÇÃO
SELECT verifica_meta_vendedor(12304136792,7,2019)