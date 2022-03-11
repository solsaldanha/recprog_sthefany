from model.Diretor import Diretor

class DiretorDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarDiretores(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM diretor ORDER BY pid'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            diretor = Diretor()
            diretor.pid = item[0]
            diretor.nome = item[1]
            diretor.email = item[2]
            diretor.num_alunos = item[4]
            diretor.idade = item[5]

            lista.append(diretor)

        return lista

    def selecionarDiretor(self, pid) -> Diretor:
        c = self.connection.cursor()
        c.execute(f"SELECT * FROM diretor WHERE pid = {pid}")
        recset = c.fetchone()
        c.close()

        print(recset)

        diretor = Diretor()
        diretor.pid = recset[0]
        diretor.nome = recset[1]
        diretor.email = recset[2]
        diretor.num_alunos = recset[4]
        diretor.idade = recset[5]
        

        return diretor

    def inserirDiretor(self, diretor: Diretor) -> Diretor:
        c = self.connection.cursor()
        c.execute("""
            insert into diretor(nome, email, num_alunos, idade)
            values('{}', '{}', '{}', '{}') RETURNING pid
        """.format(diretor.nome, diretor.email, diretor.num_alunos, diretor.idade))

        self.connection.commit()

    def alterarDiretor(self, diretor: Diretor) -> Diretor:
        c = self.connection.cursor()
        c.execute("""
            update diretor
            SET nome = '{}', email = '{}', num_alunos = '{}', idade = '{}'
            WHERE pid = '{}';
        """.format(diretor.nome, diretor.email, diretor.num_alunos, diretor.idade, diretor.pid))

        self.connection.commit()

    def excluirDiretor(self, diretor: Diretor) -> Diretor:
        c = self.connection.cursor()
        c.execute("""
            delete from diretor
            where pid = '{}'
        """.format(diretor.pid))
        self.connection.commit()