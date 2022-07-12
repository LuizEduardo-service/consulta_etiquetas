import os
import time
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from os.path import getmtime
from glob import iglob
from etiquetas.data import DataBase
from etiquetas.consulta_etiqueta import ConsultaEtiqueta

root = Tk()
COLOR_BT_PRIMARIO = '#FFA051'
COLOR_BT_SECUNDA = '#131047'
FONT_BT_SECUNDA = '#FFFFFF'
BG_COLOR = '#F5F5FF'
FONT_TEXT = ('Poppins', 10)
FONT_BT = ('Poppins', 10, 'bold')
BULLET = '•'
class TelaSitema:

    
    def __init__(self) -> None:
        self.root = root
        self.db = DataBase()
        self.imagem_layout()
        self.lista_comp_validacao()
        self.tela()
        self.root.mainloop()

    def lista_comp_validacao(self):
        self.valida_comp_config = []
        self.valida_comp_usuario = []

    def imagem_layout(self):
        self.parentDirectory = os.path.dirname(os.getcwd())
        dir_image = os.path.join(self.parentDirectory, 'image\\')
        self.image_config =  PhotoImage(file=dir_image + 'config.png')   
        self.image_tela_inicial =  PhotoImage(file=dir_image + 'telaInicial.png')   
        self.image_usuario =  PhotoImage(file=dir_image + 'usuario.png')   
        self.image_bt_config = PhotoImage(file=dir_image + 'icon_config.png',width=38, height=38)     
        self.image_bt_play = PhotoImage(file=dir_image + 'icon_play.png',width=38, height=38)     
        self.image_bt_usuario = PhotoImage(file=dir_image + 'icon_usuario.png',width=38, height=38)
        self.image_bt_visivel = PhotoImage(file=dir_image + 'visivel.png',width=30, height=30)

    def centralizar_tela(self, largura, altura):
        param = []

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        posX = (largura_tela/2) - (largura/2)
        posY = (altura_tela/2) - (altura/2)

        param.append(largura);param.append(altura);param.append(posX);param.append(posY)
        return param

    def tela(self):
        self.root.title('Etiquetas Correios')
        pos = self.centralizar_tela(600,400)
        self.root.geometry("%dx%d+%d+%d" % (pos[0],pos[1],pos[2],pos[3]))
        self.componentes_tela_inicial()
        
    



    def destruir_componentes(self):
        for comp in self.root.winfo_children():
            comp.destroy()

    def componentes_botoes_principais(self):

        self.bt_config = Button(self.root,
                                image=self.image_bt_config,
                                cursor='hand2',
                                border=False,
                                bg=COLOR_BT_PRIMARIO,
                                activebackground=COLOR_BT_PRIMARIO,
                                command=lambda:self.componentes_config()
                                )
        
        self.bt_play = Button(self.root,
                                image=self.image_bt_play,
                                cursor='hand2',
                                border=False,
                                bg=COLOR_BT_PRIMARIO,
                                activebackground=COLOR_BT_PRIMARIO,
                                command=lambda:self.componentes_tela_inicial()
                                )
        
        self.bt_usuario = Button(self.root,
                                image=self.image_bt_usuario,
                                cursor='hand2',
                                border=False,
                                bg=COLOR_BT_PRIMARIO,
                                activebackground=COLOR_BT_PRIMARIO,
                                command=lambda:self.componentes_usuario()
                                )

        self.bt_config.place(x=90,y=333,width=38,height=38)
        self.bt_play.place(x=283,y=333,width=38,height=38)
        self.bt_usuario.place(x=476,y=333,width=38,height=38)

    def componentes_config(self):
        self.lista_comp_validacao()
        self.destruir_componentes()
        self.label_image = Label(self.root,image=self.image_config)
        self.label_image.place(x=0,y=0)

        self.var_diretorio = StringVar()
        self.var_nome_arquivo = StringVar()
        self.var_dir_saida = StringVar()
        self.var_nome_arq_saida = StringVar()

        self.diretorio = Entry(self.root, 
                                font=FONT_TEXT, 
                                textvariable=self.var_diretorio,)

        self.nome_arquivo = Entry(self.root, 
                                font=FONT_TEXT, 
                                textvariable=self.var_nome_arquivo)

        self.dir_saida = Entry(self.root, 
                                font=FONT_TEXT, 
                                textvariable=self.var_dir_saida)

        self.nome_arq_saida = Entry(self.root, 
                                font=FONT_TEXT, 
                                textvariable=self.var_nome_arq_saida)
        
        self.valida_comp_config.append(self.diretorio)
        self.valida_comp_config.append(self.nome_arquivo)
        self.valida_comp_config.append(self.dir_saida)
        self.valida_comp_config.append(self.nome_arq_saida)
        
        self.diretorio.place(x=63, y=117, width=232, height=21)
        self.nome_arquivo.place(x=353, y=117, width=162, height=21)
        self.dir_saida.place(x=63, y=216, width=232, height=21)
        self.nome_arq_saida.place(x=353, y=215, width=162, height=21)

        self.bt_pesq_dir = Button(self.root,
                                    text='...', 
                                    font=('Poppins', 10, 'bold'),
                                    cursor='hand2',
                                    justify='center',
                                    command=lambda:self.define_diretorio(1))

        self.bt_pesq_dir_saida = Button(self.root,
                                    text='...', 
                                    font=('Poppins', 10, 'bold'),
                                    cursor='hand2',
                                    justify='center',
                                    command=lambda:self.define_diretorio(2))

        self.bt_salvar_config = Button(self.root,
                                    text='SALVAR',
                                    bg=COLOR_BT_SECUNDA,
                                     fg=FONT_BT_SECUNDA,
                                    font=FONT_BT,
                                    cursor='hand2',
                                    justify='center',
                                    command=lambda:self.salvar_configuracoes())


        self.bt_pesq_dir.place(x=306, y=117, width=34, height=21)
        self.bt_pesq_dir_saida.place(x=306, y=216, width=34, height=21)
        self.bt_salvar_config.place(x=224, y=260, width=153, height=30)
        self.componentes_botoes_principais()
        self.carregar_dados_config()

    def componentes_usuario(self):
        self.lista_comp_validacao()
        self.destruir_componentes()
        lb_imagem = Label(self.root, image=self.image_usuario)
        lb_imagem.place(x=0, y=0)

        self.var_usuario = StringVar()
        self.var_senha = StringVar()


        self.usuario = Entry(self.root, 
                                font=FONT_TEXT, 
                                textvariable=self.var_usuario)
        self.senha = Entry(self.root, 
                                font=FONT_TEXT, 
                                show=BULLET,
                                textvariable=self.var_senha)

        self.usuario.place(x=80, y=158, width=183, height=21)
        self.senha.place(x=332, y=158, width=111, height=21)
                                
        self.valida_comp_usuario.append(self.usuario)
        self.valida_comp_usuario.append(self.senha)

        self.ver_senha = Button(self.root,
                                    image=self.image_bt_visivel,
                                    cursor='hand2',
                                    border=False,
                                    activebackground=BG_COLOR,
                                    bg=BG_COLOR,
                                    command=lambda:self.mostra_senha(self.senha))

        self.bt_salvar_usuario = Button(self.root,
                                    text='SALVAR',
                                    bg=COLOR_BT_SECUNDA,
                                     fg=FONT_BT_SECUNDA,
                                    font=FONT_BT,
                                    cursor='hand2',
                                    justify='center',
                                    command=lambda:self.salvar_usuario())
        
        self.ver_senha.place(x=459, y=151, width=33, height=30)
        self.bt_salvar_usuario.place(x=217, y=211, width=153, height=30)
        self.componentes_botoes_principais()
        self.carregar_dados_usuario()

    def componentes_tela_inicial(self):
        self.lista_comp_validacao()
        self.destruir_componentes()
        lb_imagem = Label(self.root,image=self.image_tela_inicial)
        lb_imagem.place(x=0, y=0)
        self.lb_status = Label(self.root,text='STATUS',bg=BG_COLOR)

        self.bt_consultar = Button(self.root,
                            text='CONSULTAR',
                            bg=COLOR_BT_SECUNDA,
                            fg=FONT_BT_SECUNDA,
                            font=FONT_BT,
                            border=False,
                            activebackground=COLOR_BT_SECUNDA,
                            activeforeground="#ffffff",
                            cursor='hand2',
                            justify='center',
                            command=lambda:self.consultar_etiquetas())

        self.bt_exp_arquivo = Button(self.root,
                            text='EXPORTAR\n ARQUIVO',
                            bg=COLOR_BT_SECUNDA,
                            fg=FONT_BT_SECUNDA,
                            font=FONT_BT,
                            border=False,
                            activebackground=COLOR_BT_SECUNDA,
                            activeforeground="#ffffff",
                            cursor='hand2',
                            justify='center',
                            command=lambda:self.exportar_arquivo())

        self.bt_consultar.place(x=61, y=136, width=156, height=118)
        self.bt_exp_arquivo.place(x=362, y=136, width=156, height=118)
        self.lb_status.place(x=128, y=85, width=338, height=26)
        self.componentes_botoes_principais()

    #variaveis de componentes
    def variaveis_config(self):
        self.v_diretorio = self.var_diretorio.get()
        self.v_nome_arquivo = self.var_nome_arquivo.get()
        self.v_dir_saida = self.var_dir_saida.get()
        self.v_nome_arq_saida = self.var_nome_arq_saida.get()
    
    def variaveis_usuario(self):
        self.v_usuario = self.var_usuario.get()
        self.v_senha = self.var_senha.get()

    #metodos de configurações
    def valida_campos_vazios(self, lista_campos: list):

        campo_validado = False
        for campo in lista_campos:
            if(len(campo.get())==0):
                campo_validado = True
                break

        if campo_validado ==True:
            messagebox.showerror('Campos Vazios', 'Existem campos em branco\nVerifique os dados e tente novamente')
            return False

        return True

    def define_diretorio(self, tipo: int) -> str:
        diretorio = askdirectory()
        if diretorio:
            if tipo == 1:
                self.var_diretorio.set(diretorio)
            elif tipo == 2:
                self.var_dir_saida.set(diretorio)

    def mostra_senha(self, campo: Tk):
        try:
            if campo.cget('show') == '':
                campo.config(show=BULLET)
            else:
                campo.config(show='')   
        except:
            pass 

    def localiza_arquivo(self, caminho, nomeArq) -> str:
            files = iglob(caminho + "\\*")
            sorted_files = sorted(files, key=getmtime, reverse=True)
            arquivo:str =''
            for f in sorted_files:
                if str(nomeArq) in f:
                    arquivo = f
                    return arquivo       
            messagebox.showerror('Erro de Arquivo',f'Nenhum arquivo com o nome de "{nomeArq}" foi localizado')
            return 

    def verifica_pasta(self, diretorio):
        if os.path.isdir(diretorio):
            return True
        else:
            messagebox.showerror('Erro de pasta','Pasta não localizada')
            return False

    def arquivo_atual(self, nomeArquivo, diretorio):


        if self.verifica_pasta(diretorio):
            l_arquivos = os.listdir(diretorio)
            l_datas = []
            for arquivo in l_arquivos:
                if nomeArquivo in arquivo:

                    data = os.path.getmtime(os.path.join(os.path.realpath(diretorio), arquivo))
                    l_datas.append((data, arquivo))
            try:
                l_datas.sort(reverse=True)
                ult_arquivo = l_datas[0]
                nome_arquivo = ult_arquivo[1]
                data_arquivo = ult_arquivo[0]
                arq = os.path.join(os.path.realpath(diretorio), nome_arquivo)
                data_mod = self.data_modificacao(arq)
                
                return [nome_arquivo, data_mod, arq]
            except:
                messagebox.showerror('Erro de Arquivo','Nenhum arquivo Localizado.')
                return 

    #ações botoes
    def salvar_configuracoes(self):
        if self.valida_campos_vazios(self.valida_comp_config):
            self.variaveis_config()

            sql ="""UPDATE tb_config SET diretorio ='{}', nome_arq ='{}', dir_saida ='{}',nome_arq_saida ='{}' WHERE id = 1
            """.format(self.v_diretorio, self.v_nome_arquivo, self.v_dir_saida, self.v_nome_arq_saida)
            self.db.update(sql)

    def salvar_usuario(self):
        if self.valida_campos_vazios(self.valida_comp_usuario):
            self.variaveis_usuario()

            sql ="""UPDATE tb_usuario SET usuario ='{}', senha = '{}' WHERE id = 1
            """.format(self.v_usuario, self.v_senha)
            self.db.update(sql)

    def consultar_etiquetas(self):
        #pegar dados do banco usuario
        dados_usuario = self.db.mostra_dados('tb_usuario')
        usuario = dados_usuario[0][1]
        senha = dados_usuario[0][2]

        #pegar dados de diretorio
        dados_diretorio = self.db.mostra_dados('tb_config')
        diretorio = dados_diretorio[0][1]
        arquivo = dados_diretorio[0][2]

        valida_local = self.arquivo_atual(arquivo, diretorio)

        if valida_local:
            arquivo = valida_local[0]
            data = valida_local[1]
            caminho = valida_local[2]
            opc = messagebox.askyesno('Arquivo Selecionado', f"""Arquivo selecionado!!!\n
            Nome arquivo: {arquivo}\n
            Data Mod: {data}\n
            Dir: {caminho}\n\n
            Continuar processo!?""")

            if opc:
                self.consulta = ConsultaEtiqueta(usuario, senha)
                status = self.consulta.start()
        
    def exportar_arquivo(self, dados: list = []):
        #pegar dados diretorio
        dados_diretorio = self.db.mostra_dados('tb_config')
        diretorio = dados_diretorio[0][3]
        arquivo = dados_diretorio[0][4]

        if self.verifica_pasta(diretorio):
            messagebox.showinfo('msg', 'Pasta verificada')

        #salvar arquivo
        

    #dados
    def carregar_dados_config(self):
        try:
            dados = self.db.mostra_dados('tb_config')
            self.var_diretorio.set(dados[0][1])
            self.var_nome_arquivo.set(dados[0][2])
            self.var_dir_saida.set(dados[0][3])
            self.var_nome_arq_saida.set(dados[0][4])
        except:
            pass

    def carregar_dados_usuario(self):
        try:
            dados = self.db.mostra_dados('tb_usuario')
            self.var_usuario.set(dados[0][1])
            self.var_senha.set(dados[0][2])
        except:
            pass
            
    def data_modificacao(self, arquivo):

            ti_m = os.path.getmtime(arquivo) 
            
            m_ti = time.ctime(ti_m) 
            t_obj = time.strptime(m_ti) 
            T_stamp = time.strftime("%d/%m/%Y %H:%M:%S", t_obj) 
            
            # print(f"The file located at the path {arquivo} was last modified at {T_stamp}")
            return T_stamp


if __name__ == '__main__':
    TelaSitema()