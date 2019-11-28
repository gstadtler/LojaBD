CREATE OR REPLACE FUNCTION insere_atualiza_deleta_cliente(
    IN vOPR CHAR,
	IN vCPF BIGINT,
    IN vNome_cliente VARCHAR(50),
    IN vEmail_cliente VARCHAR(20),
	IN vRua_cliente VARCHAR(20),
	IN vNumero_cliente INTEGER,
	IN vBairro_cliente VARCHAR(20),
	IN vCidade_cliente VARCHAR(20)) 
	RETURNS void AS $$
BEGIN   
  IF (vOPR = 'I') THEN
    INSERT INTO cliente(cpf,nome_cliente,
						email_cliente,rua_cliente,
						numero_cliente,bairro_cliente,
						cidade_cliente
					    ) VALUES (vCPF,vNome_cliente,
								  vEmail_cliente,vRua_cliente,
								  vNumero_cliente,vBairro_cliente,
								  vCidade_cliente);
  ELSE
  IF(vOPR = 'A') THEN
    UPDATE cliente SET nome_cliente = vNome_cliente,
	email_cliente = vEmail_cliente, rua_cliente = vRua_cliente,
	numero_cliente = vNumero_cliente, bairro_cliente = vBairro_cliente,
	cidade_cliente = vCidade_cliente WHERE cpf = vCPF;
  ELSE
  IF(vOPR = 'D')THEN
    DELETE FROM cliente WHERE cpf = vCPF;
  ELSE
    RAISE EXCEPTION 'ATENÇÃO! Operação diferente de I, D, A.';
  END IF;
  END IF;
  END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insere_atualiza_deleta_funcionario(
    IN vOPR CHAR,
	IN vCPF BIGINT,
    IN vNome_funcionario VARCHAR(50),
    IN vEmail_funcionario VARCHAR(20),
	IN vSenha_funcionario VARCHAR(20))
	RETURNS void AS $$
BEGIN   
  IF (vOPR = 'I') THEN
    INSERT INTO funcionario(cpf,nome,email,senha) VALUES (vCPF,vNome_funcionario,
								  						  vEmail_funcionario,vSenha_funcionario);
  ELSE
  IF(vOPR = 'A') THEN
    UPDATE cliente SET nome = vNome_funcionario,
	email = vEmail_funcionario, 
	senha = vSenha_funcionario WHERE cpf = vCPF;
  ELSE
  IF(vOPR = 'D')THEN
    DELETE FROM funcionario WHERE cpf = vCPF;
  ELSE
    RAISE EXCEPTION 'ATENÇÃO! Operação diferente de I, D, A.';
  END IF;
  END IF;
  END IF;
END;
$$ LANGUAGE plpgsql;