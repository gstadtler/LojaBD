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
	IN vSenha_funcionario VARCHAR(20),
	IN vFlag_gerente BOOL)
	RETURNS void AS $$
BEGIN
    IF (vOPR = 'I') THEN
      INSERT INTO funcionario(cpf,nome,email,senha,flag_gerente) VALUES (vCPF,vNome_funcionario,
								  						  vEmail_funcionario,vSenha_funcionario,
													      vFlag_gerente);
	  IF(vFlag_gerente = True) THEN
	    INSERT INTO gerente VALUES (vCPF);
	  ELSE IF(vFlag_gerente = False) THEN                                               
	    INSERT INTO vendedor VALUES (vCPF,49709849050,10);
	  COMMIT;
	  ELSE
	    RAISE EXCEPTION 'Ocorreu algum problema...';
		ROLLBACK;
	  END IF;
	  END IF;

    ELSE IF(vOPR = 'A') THEN
      UPDATE funcionario SET nome = vNome_funcionario, email = vEmail_funcionario, 
	  senha = vSenha_funcionario, flag_gerente = vFlag_gerente WHERE cpf = vCPF;
	
    ELSE IF(vOPR = 'D')THEN
	  IF(vFlag_gerente = True) THEN
	  	DELETE FROM gerente WHERE cpf = vCPF;
      	DELETE FROM funcionario WHERE cpf = vCPF;
	  ELSE IF(vFlag_gerente = False) THEN
	    DELETE FROM vendedor WHERE cpf = vCPF;
		DELETE FROM funcionario WHERE cpf = vCPF;
	  COMMIT;
	  ELSE
	    RAISE EXCEPTION 'Ocorreu algum problema...';
		ROLLBACK;
	  END IF;
	  END IF;
	ELSE
	  RAISE EXCEPTION 'Atenção! Operação diferente de I, A ou D.';
  END IF;
  END IF;
  END IF;
END;
$$ LANGUAGE plpgsql;
