"""
This module provides tools for debt negotiation operations.
"""

from datetime import datetime

from langchain.tools import tool

from db import get_db_connection


class NegociacaoTools:
    """
    Classe que contém ferramentas para negociação de dívidas.
    """

    @tool("consultar_cpf")
    def consultar_cpf(cpf: str) -> dict:
        """
        Consulta os dados de um cliente a partir do CPF.

        Parâmetros:
            cpf (str): CPF do cliente a ser consultado.

        Retorna:
            dict: Um dicionário com as chaves 'id' e 'nome' do devedor, ou um
            dicionário vazio se não encontrado.

        Uso:
            Sempre que precisar iniciar uma negociação ou consultar dados do
            cliente, utilize esta ferramenta.
        """
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT id, nome
                from devedores
                where cpf_cnpj = %s;""",
                (cpf,),
            )
            result = cursor.fetchone()

        return result or {}

    @tool("ver_divida")
    def ver_divida(devedor_id: int) -> float:
        """
        Consulta o valor total das dívidas pendentes de um devedor.

        Parâmetros:
            devedor_id (int): ID do devedor.

        Retorna:
            float: Valor total das dívidas pendentes. Retorna 0 se não houver
            dívidas.

        Uso:
            Utilize após consultar o CPF e obter o ID do devedor.
        """
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT sum(valor) as total
                from dividas
                where devedor_id = %s;""",
                (devedor_id,),
            )
            result = cursor.fetchone()

        return float(result.get("total", 0)) if result else 0.0

    @tool("ver_acordo")
    def ver_acordo(devedor_id: int) -> float | str:
        """
        Verifica se existe um acordo ativo para o devedor e retorna seu valor.

        Parâmetros:
            devedor_id (int): ID do devedor.

        Retorna:
            float | str: Valor do acordo ativo se existir, ou uma mensagem
            indicando que não há acordo.

        Uso:
            Utilize após consultar o CPF e obter o ID do devedor.
        """
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT valor_acordo
                FROM acordos a
                JOIN dividas d ON a.divida_id = d.id
                WHERE d.devedor_id = %s AND a.cancelado = FALSE
                ORDER BY a.data_acordo DESC LIMIT 1""",
                (devedor_id,),
            )
            result = cursor.fetchone()

        return result.get("valor_acordo") if result else "Nenhum acordo encontrado."

    @tool("registrar_acordo")
    def registrar_acordo(
        devedor_id: int,
        negociador_id: int,
        valor_acordo: float,
        qtd_parcelas: int,
    ) -> str:
        """
        Registra um novo acordo para um devedor.

        Parâmetros:
            devedor_id (int): ID do devedor.
            negociador_id (int): ID do negociador responsável.
            valor_acordo (float): Valor total do acordo.
            qtd_parcelas (int): Quantidade de parcelas do acordo.

        Retorna:
            str: Mensagem de sucesso ou erro.

        Uso:
            Utilize após consultar CPF e dívida, quando o cliente aceitar um
            acordo.
        """
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id
                FROM dividas
                WHERE devedor_id = %s
                ORDER BY data_venc DESC LIMIT 1
                """,
                (devedor_id,),
            )
            divida = cursor.fetchone()
            if not divida:
                return "Nenhuma dívida encontrada para registrar acordo."

            cursor.execute(
                """
                INSERT INTO acordos
                (divida_id, negociador_id, valor_acordo, qtd_parcelas, data_acordo)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    divida["id"],
                    negociador_id,
                    valor_acordo,
                    qtd_parcelas,
                    datetime.now().date(),
                ),
            )
            conn.commit()

        return "Acordo registrado com sucesso."
