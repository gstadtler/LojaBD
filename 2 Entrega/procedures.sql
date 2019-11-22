CREATE PROCEDURE insere_atualiza_deleta_cliente(
    vOPR CHAR
	vCPF BIGINT,
    vNome_cliente VARCHAR(50),
    vEmail_cliente VARCHAR(20),
	vRua_cliente VARCHAR(20),
	vNumero_cliente INTEGER,
	vBairro_cliente VARCHAR(20),
	vCidade_cliente VARCHAR(20))
IS 
    vEXCEPTION EXCEPTION;
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
    RAISE vEXCEPTION;
  END IF;
  END IF;
  END IF;
  EXCEPTION
    WHEN vEXCEPTION THEN
      RAISE_APPLICATION_ERROR(-20999,'ATENÇÃO! Operação diferente de I, D, A.', FALSE);
END insere_atualiza_deleta_cliente;