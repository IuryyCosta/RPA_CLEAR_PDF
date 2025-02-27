Guia da Função CPOE   
Computerized Provider  
Order Entry

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


1 Apresentação da Função CPOE  
A função CPOE é utilizada para realizar as prescrições dos pacientes e tem como objetivo facilitar a adoção e o uso  
por profissionais da área assistencial  
A CPOE possui várias funcionalidades sendo a principal delas a Auto complete onde quando o usuário escreve  
o nome do medicamento o sistema mostra automaticamente o restante da palavra  
11 Principais Caraterísticas  
 Interface intuitiva e objetiva buscando a padronização de regras e fluxos ao prescrever itens  
 A hierarquia da informação foi escolhida para que a adoção da ferramenta e o entendimento sejam mais  
rápidos Precisão de escolha para os elementos que aparecem em destaque para o usuário e precisão na  
organização da informação  
 Novo conceito de Plano Terapêutico Visibilidade dos tratamentos para todos os profissionais que de  
alguma forma irão interagir com o paciente  
 O uso do Auto complete dá agilidade ao processo pois o sistema automaticamente sugere resultados  
conforme as primeiras letras digitadas de nomes medicamentos etc  
 Definição de itens que serão mantidos até 2ª ordem ou seja sem data de fim facilita a prescrição de  
itens que o paciente utiliza diariamente como medicamentos de uso contínuo  
 Prazo de validade por item onde elimina a necessidade de fazer cópias ou extensões agilizando a rotina  
do profissional  
 Consolida na tela de liberação o que foi inserido modificado ou descontinuado dando opção de realizar  
uma segunda avaliação antes de liberar a prescrição  
 Tela de apoio Log ações com o resumo dos acontecimentos recentes adicionado suspenso  
modificado responsável data e hora e ações previstas para o futuro próximo  
Todos os campos do Tasy possuem o recurso de infobutton como destacado na tela abaixo Este recurso é  
utilizado para saber mais detalhes sobre o campo e o tipo de informação a ser inserida no momento da utilização da  
função  


2 Principais cadastros  
A seguir serão descritos os cadastros prévios que devem ser realizados antes de iniciar o uso da função CPOE  
21 JOBs necessárias  
211 Job responsável por atualizar o passado  
VARIABLE JOBNO NUMBER  
BEGIN  
DBMS_JOBSUBMITJOBNO  
CPOE_GERAR_REG_JSONTASY  
SYSDATE  
TruncSYSDATE  1  0824  
  
END  
  
212 Job responsável pela cópia automática das prescrições conforme validade  
variable jobno number  
begin  
dbms_jobsubmitjobno  
cpoe_copiar_itens_atendsysdateTASY21331  
truncsysdatehh24 124  
truncsysdatehh24  124  
  
end  
  
Observação O parâmetro 2133 deve ser substituído pelo código do perfil que existem as parametrizações da REP  


Principais campos  
 Regra contempla todos os grupos da prescrição onde cada pode ser configurado da seguinte forma  
o Permite Prescrever Marque se o grupo pode ser prescrito  
o Somente Visualizar Marque se o grupo somente será visualizado sem permitir inclusão e edição  
o Não Apresenta Marque se o grupo não será apresentado  
 Visualizar pedidos de cirurgia Marque se itens cirúrgicos serão apresentados  
 Funções de usuários que devem ser apresentadas no grid Informe o item que será apresentado conforme  
função do prescritor  
23 Regra de ordenação  
Neste cadastro podemse definir regras de ordenação para apresentação dos itens na CPOE  
Para realizar o cadastro é necessário acessar a função Cadastros PEP  Regra Ordenação CPOE e definir o nome  
da regra  
Assim que cadastrado o nome da regra é necessário realizar duplo clique sobre o registro Assim será exibida a tela  
Regra de ordenação dos grupos para cadastrar os itens que serão exibidos e sua ordem de apresentação  
Principais campos  
 Grupo Selecione o grupo que terá a regra de ordenação cadastrada  
 Ordem apresentação Informe a ordem de apresentação do grupo  
 Apresentar itens ACMSN somente ao final do grupo Marque se os itens prescritos como ACM a critério  
médico eou SN se necessário deverão serem exibidos ao final do grupo  
 Mesma sequência da REP Marque se os itens devem ser apresentados na mesma sequência da CPOE  
Na aba Regra ordenação medicamentos CPOE caso desejado é possível cadastrar a ordem de apresentação de  
acordo com medicamento grupo de medicamentos subgrupo de medicamentos classe de medicamentos ou via de  
administração Para realizar este cadastro é necessário realizar duplo clique sobre o grupo da CPOE Ao realizar  
esta ação o sistema exibe a tela Regra de ordenação medicamentos CPOE  
Principais campos  
 Medicamento Informe o medicamento que atende a regra  
 Grupo de medicamentos Informe o grupo de medicamento que atenda a regra  
 Subgrupo de medicamentos Informe o subgrupo de medicamento que atenda a regra  
 Classe de medicamentos Informe a classe de medicamento que atende a regra  
 Via de aplicação Selecione a via de aplicação que atende a regra  
 Ordem apresentação Informe a ordem que será apresentado este registro  


Benefícios  
 Aumentar a segurança dos pacientes  
 Como o prescritor que valida a prescrição diária pode ser diferente do prescritor inicial cada validação  
garante e armazena as informações do responsável por aquele ato  
 Gestão de confirmação de itens críticospotencialmente perigosos ação positiva do médico confirmando  
itens potencialmente perigosos  
 Transparência no ADEP facilidade para a equipe de enfermagem ter um gerenciamento sobre os itens do  
plano que estão com risco de expiração da validade possibilidade na tomada de ações  
 Rastreabilidade visão transparente em cima de todos os eventos de revalidação no plano terapêutico  
Principais funcionalidades  
 Permitir definição de um prazo para revalidação dos itens da CPOE  
 Permitir que um médico revalide um plano e assuma todo o plano caso ele não fosse o prescritor original  
 Permitir revalidação parcial do plano  
 Exibir os itens que terão sua validade expirada  
 A necessidade de revalidação pode ser comunicada via email ou comunicação interna  
 Itens críticos ou potencialmente perigosos podem ter uma tratativa diferenciada exigindo uma nova  
confirmação  
 Todas as ações relacionadas à revalidação ficarão registradas no loggerenciador de revalidações na CPOE  
241 Regra de Revalidação da CPOE  
Para realizar o cadastro é necessário acessar a função Cadastros gerais  Aplicação Principal  Médico  
Prescrição  Regra de Revalidação da CPOE  
Principais campos  
 Perfil Informe o perfil que a regra se aplique  
 Setor Informe o setor que a regra se aplique  
 Médico Informe o médico que a regra se aplique  
 Dias Informe os dias que o item será revalidado  
 Hora Informe o horário de corte da revalidação  
 Horas Anteriores Informe a quantidade de horas anteriores que o médico poderá reavalidar o item  


 Subgrupo de medicamentos Informe o subgrupo de medicamento que atende a regra  
 Classe de medicamentos Informe a classe de medicamento que atende a regra  
243 Usuários destinos  
Na aba Usuários destinos é possível cadastrar usuários que serão notificados caso itens não serem revalidados de  
acordo com a regra  Regra de Revalidação da CPOE  
Principais campos  
 Perfil Informe o perfil que a regra se aplique  
 Usuário Informe o usuário que a regra se aplique  
 Forma envio Selecione a forma que usuário será notificado  
 Horas Informe a quantidade de horas posteriores a revalidação que será disparado a notificação  
 Email remetente Informe o email caso forma de envio da notificação seja email  
 Mensagem Informe uma mensagem padrão que será enviada na notificação  
25 Regra de abertura automática de rotina  
Neste cadastro podemse definir os grupos da prescrição que terá a tela de rotinas aberta automaticamente  
Para realizar o cadastro é necessário acessar a função Cadastros gerais  Aplicação Principal  Médico  
Prescrição  CPOE  Regra de abertura automática da tela de rotina dos itens  
Principais campos  
 Perfil Informe o perfil que a regra se aplique  
 Setor Informe o setor que a regra se aplique  
 Abrir função Marque se a tela de rotinas deve ser apresentada ao abrir função  
Regra contempla todos os grupos da prescrição onde cada pode ser configurado da seguinte forma  
o Não Permite Define que a tela de rotina não será aberta automaticamente  
o Permite Define que a tela de rotina será aberta automaticamente  
o Permite e bloqueia autocomplete Define que a tela de rotina será aberta automaticamente e não  
será permitido prescrição utilizando autocomplete  
26 Função Cadastro de materiais  
Os cadastros dos medicamentos soluções dietas industrializadas suplementos nutricionais deverão estar  
adequadamente informados nesta função As informações como diluente reconstituinte e rediluente também são  
provenientes desta função para que sejam apresentadas na CPOE  


Os cadastros são realizados pelo cliente na função Prontuário Eletrônico do Paciente PEP  item Cadastros  
gerais  Intervalo da prescrição Porém somente os cadastros ativos serão apresentados  
Todos os cadastros poderão ser prescritos A critério médico ACM Se necessário SN Agora e poderão ter  
esquema de doses diferenciadas  
Para que um intervalo não seja apresentado em um grupo específico da prescrição devese cadastrar uma regra de  
exclusão na aba Regra Do contrário serão apresentados em todos os grupos Nutrição Soluções e medicamentos  
Exames e procedimentos Gasoterapia Recomendações  
28 Processo para prescrição de Soluções e Medicamentos  
A prescrição de soluções e medicamentos é realizada em um mesmo local através de um mesmo localizador O  
usuário deverá selecionar o item a ser prescrito De acordo com as regras o sistema apresentará a estrutura de  
prescrição para soluções ou medicamentos  
281 Informações principais  
É possível buscar o a solução ou o medicamento através do localizador De acordo com o cadastro do item o sistema  
automaticamente apresentará somente os campos apropriados ao tipo do medicamento selecionado Caso  
adicionado mais um item componente e este item não possuir a via de administração utilizada para o primeiro item  
prescrito item principal o sistema apresentará uma consistência e não permitirá a inclusão deste item  
282 Período de vigência  
É possível cadastrar o intervalo onde o recomendado é que seja cadastrado uma opção de intervalo para o item  
para que seja a opção padrão Além disso conforme características do medicamento podese definir intervalos  
sugeridos função Cadastro de materiais  Farmácia  Intervalos sugeridos onde somente os intervalos  
cadastrados neste local serão apresentados no campo Intervalo da prescrição  
Principais campos  
 Início Informe a data e em qual horário a primeira aplicação do produto deve ocorrer O sistema calculará  
os demais horários de acordo com o intervalo prescrito Todo item prescrito inicia no momento em que é  
liberado no sistema  
 Administração Selecione a forma na qual o intervalo de aplicação do produto deve ocorrer opções  
Conforme 1º horário Se necessário A critério médico  
 Agora Marque se há urgência para iniciar a administraçãoexecução do item prescrito  
 Término Selecione o período de vigência do item Se o item deverá manterse na prescrição até nova  
definição do médico responsável Mantido até 2ª ordem ou se terá uma data de fim Programada O  
sistema respeitará esta definição do usuário médico e gerará automaticamente as cópias de prescrições  


 Observação Forneça informações adicionais sobre as soluções eou medicamentos do paciente se  
necessário  
 Justificativa Conforme exigências do processo justificativa de uso por exemplo o sistema gera uma  
obrigatoriedade de preenchimento para o prescritor no momento da consistência e salva os registros  
neste campo  
284 Quando o item prescrito for tratado como solução  
2841 Informações principais  
É possível buscar o item através do localizador De acordo com o cadastro do item o sistema automaticamente  
apresentará somente os campos apropriados ao tipo do item selecionado Caso adicionado mais um item  
componente e este item não possua a via de administração utilizada para o primeiro item prescrito item principal  
o sistema apresentará uma consistência e não permitirá a inclusão deste item  
2842 Informações de administração  
O sistema apresentará um radiogroup para selecionar o tipo de solução desejado para a prescrição contínua  
intermitente velocidade variável e PCA analgesia controlada pelo paciente Conforme regra definida na função  
Cadastro de materiais  aba Presc  Tipo de solução CPOE o sistema já apresentará esta opção default e os  
demais campos necessários referente à solução selecionada  
3 Principais Parâmetros  
Tabela Parâmetros da função CPOE  
Número Descrição Explicação  
1 Número de horas anteriores para cópia dos Define número de horas anterior ao  
itens horário de administração do item  
para a cópia ser realizada Neste  
parâmetro devem ser utilizados  
valores de 6 a 12 horas Caso seja  
preenchido valor maior ou menor  
que os valores mencionados o  
sistema irá jogar sempre 12 caso seja  
maior ou 6 caso seja menor  
7 Utilizar integrações de base de dados de Valida se há integrações configuradas  
medicamentos durante a prescrição e compatíveis com a função  
8 Forma de geração da data fim para os itens Define a forma da data fim dos itens  


4 Função CPOE  
41 Localizador de pacientes  
As informações dos pacientes apresentadas no localizador de pacientes são decorrentes das informações Cadastro  
completo de pessoas Cadastro simplificado de pessoas e Entrada única de pacientes  
  
resultados  
43 Atendimento  
Ao selecionar a opção Atendimento e digitar o número do atendimento desejado o sistema apresenta o paciente  
com o atendimento informado  
44 Setor  
Ao clicar nesta opção o sistema apresenta um popup para selecionar o setor selecionado Após selecionado um  
setor o sistema apresenta a relação dos pacientes internados no setor selecionado  
45 Selecionando um paciente  
Para selecionar um paciente é necessário ir até a área que apresenta os registros e clicar sobre o atendimento  
desejado Após clicar o sistema fecha a tela de seleção de pacientes e carrega os dados do paciente na tela da  
prescrição  
46 Adicionar itens a prescrição  
Há duas formas de realizar a inclusão de itens na prescrição através do ícone de  no início de cada grupo de  
prescrição ou através das opções Adicionar novo Rotinas Protocolos Favoritos presente na parte superior da  
tela  


48 Timeline  
Ao lado da lista de itens prescritos é apresentada uma linha do tempo que exibe os aprazamentos e checagens de  
ações realizadas na função ADEP Administração Eletrônica da Prescrição O objetivo desta funcionalidade é a  
apresentação de uma visão dos itens aprazados e checados  
A visão atual apresenta 6 horas do passado e 18 horas do futuro como padrão do sistema podendo ser reduzido em  
até 2 horas no passado e 22 horas no futuro Conforme as horas passam o sistema atualiza as informações na tela  
e portanto um item prescrito no passado que foi descontinuado não aparecerá mais na lista  
49 Grid  
É possível consultar as principais informações dos itens tais como data de início data fim prevista data de  
descontinuação no Grid  
410 Adicionar novo  
Através desta opção o usuário poderá selecionar protocolos rotinas itens favoritos prescrições anteriores  
medicamentos em uso do paciente e prescrições especiais  
Ao selecionar os itens através do checkbox os itens selecionados são enviados para o grupo de itens selecionados  
que funciona como um carrinho de compras de itens que serão enviados para a lista da prescrição No painel de  
itens selecionados caso clicar no checkbox de um item ele é automaticamente removido da lista de selecionados  
Neste local caso o item esteja marcado com um ícone vermelho significa que o item possui campos obrigatórios  
pendentes de preenchimento  
Após selecionar todos os itens necessários o usuário deverá clicar em Ir para detalhes Neste local são  
apresentados os detalhes de todos os itens previamente selecionados  
Observação Os itens selecionados somente poderão ser enviados para a prescrição quando não houver campos  
pendentes de preenchimento Para enviálos à lista da prescrição devese clicar em Enviar para a prescrição  
4101 Protocolos  
Ao selecionar está opção é possível prescrever itens através dos protocolos précadastrados  
4102 Rotinas  
Ao selecionar está opção é possível prescrever as rotinas conforme grupos da prescrição  


4104 Prescrição Anteriores  
Ao selecionar está opção é possível prescrever itens em prescrições anteriores deste paciente  
4105 Medicamentos em Uso  
Ao selecionar está opção é possível prescrever medicamentos em uso o paciente  
4106 Dose adicional  
Através deste processo será possível administrar um horário adicional com uma dose igual ou diferente da dose  
convencional Ao selecionar Dose adicional em adicionar o sistema solicitará a dose e o horário desejado para essa  
dose adicional Desta forma o sistema irá considerar que a dose adicional respeitará o horário selecionado pelo  
prescritor e não o intervalo da dose convencional A dose adicional é única portanto caso o item seja mantido por  
mais dias nos próximos dias o sistema manterá para todos os horários a dose convencional Ao liberar este item na  
lista o item é representado duplicado com representação de que um deles tratase da dose adicional  
Importante a dose adicional é considerada uma dose complexa sendo assim caso troque a hora a hora no decorrer  
da inclusãomodificaçãodescontinuação dos itens esse item não será recalculado para próxima hora cheia Será  
necessário ir no detalhe do item e ajustar os horários  
4107 Dose de ataque  
Através deste processo será possível definir uma dose diferente maior para a primeira dose prescrita Caso o item  
tenha diluente o volume também poderá ser editado Caso se trate de um medicamento de via intravenosa também  
será possível definir um tempo de infusão Desta forma o sistema irá considerar que a dose de ataque será a primeira  
e respeitará o intervalo selecionado pelo prescritor A dose de ataque é única portanto caso o item seja mantido  
por mais dias nos próximos dias o sistema manterá para todos os horários a dose convencional Ao liberar este item  
na lista o item é representado duplicado com representação de que um deles tratase da dose de ataque  
411 Favoritos  
No detalhe de cada item e após preencher todos os campos obrigatórios o usuário poderá selecionar um item como  
favorito  
412 Gerenciamento de Favoritos  
Neste local o usuário pode visualizar todos os itens definidos como favoritos É possível visualizálos em modo de  
detalhe e excluílos da lista caso necessário O usuário não poderá editálo na tela de gerenciamento somente ao  
inserilo na prescrição  
413 Data início prescrição  
Na prescrição em HTML5 a data início da prescrição é sempre a próxima hora cheia Caso no decorrer da  
inclusãomodificaçãodescontinuação troque a hora o sistema irá perguntar Existem horários inferiores à data  


atual Deseja recalculálos para próxima hora cheia Caso concorde o sistema irá recalcular o horário de início da  
prescrição  
414 Botão Liberar  
Todas as ações na nova prescrição deverão ser liberadas inclusões modificações e descontinuações de itens  
Somente itens não liberados poderão ser excluídos da lista e portanto não precisam de liberação pois não entraram  
em vigência  
Todos os itens incluídos modificados ou itens que serão descontinuados serão representados com ícones na lista  
relógio verde para novo item prescrito lápis representa um item que sofreu modificaçãoalteração ou seja é o  
mesmo item porém com alterações círculo vermelho representa um ícone que será descontinuado suspenso  
Desta forma todos os itens que possuem estes ícones estão pendentes de liberação Ao lado do botão Liberar  
será apresentado um número que representa a quantidade de itens pendentes de liberação  
415 Botão Remover  
Para realizar a exclusão itens não liberados no sistema portanto rascunhos de um ou vários itens da prescrição o  
usuário deverá selecionar os items através do checkbox e clicar no botão Remover  
Conceitos importantes  
Remover excluir um item pendente de liberação da lista da prescrição  
Descontinuar remover suspender um item da prescrição para itens já em vigêncialiberados  
416 Prescrição de itens  
4161 Recomendações  
Para prescrever devese clicar no ícone  ao lado do título do grupo Recomendações Assim o sistema abrirá a  
tela em modo de detalhe e configurará no 1º campo Recomendação Neste campo o usuário irá informar qual  
recomendação desejada para prescrever e o sistema apresentará as opções através de um novo mecanismo de  
busca o auto complete  
As recomendações são provenientes do cadastro localizado no caminho Cadastros Gerais  Aplicação principal   
Médico  Classificação Recomendação  aba Tipo de Recomendação  
O usuário deverá então informar quando a recomendação deverá entrar em vigência início e se será mantida de  
horário se necessário ou a critério médico Em seguida deverá informar se o item será mantido na prescrição até 2ª  
ordem ou se deseja informar uma datahora de término programada Após salvar o registro o item será adicionado  
na lista da prescrição e ficará pendente de liberação  


Na prescrição após informar o dispositivo de infusão o usuário informará se a administração do gás será de forma  
contínua ou intermitente A administração contínua indica uma administração contínua em 24 horas Os intervalos  
para este item deverão ter a descrição 1xdia ou Contínuo sendo que no cadastro de intervalos Cadastros  
Gerais PEP  Intervalo da prescrição recomendase que seja um intervalo exclusivo Gasoterapia com o checkbox  
intervalo contínuo marcado Na aba Regra devese configurar GASOTERAPIA  CPOE exibir  
A administração Intermitente indica a administração do gás conforme um intervalo selecionado e possui uma pausa  
entre uma administração e outra Desta forma além do intervalo o usuário deverá informar a duração da  
administração hmin Os intervalos cadastrados para esta forma de administração de gases deverão proceder  
conforme a administração contínua Entretanto o checkbox Intervalo contínuo deverá estar desmarcado  
Conforme o tipo de respiração selecionada o sistema apresentará campos adicionais É o caso da prescrição de  
ventilação mecânica não invasiva e invasiva Em ambas será apresentado o campo modalidade respiratória No  
cadastro referente às modalidades respiratórias Cadastros gerais  Aplicação principal  Médico   
Modalidade respiratória cadastrar as modalidades utilizadas na instituição e vinculálas a um tipo de respiração  
Na prescrição o sistema apresentará campos adicionais de acordo com o tipo de respiração e modalidade  
respiratória selecionadas Os campos adicionais apresentados são campos não obrigatórios que possibilitam o  
usuário incluir informações adicionais parâmetros ventilatórios para a ventilação mecânica prescrita para o  
paciente  
Campos adicionais não obrigatórios  
 Freq prog ciclosmin Informe a frequência programada do ventilador em ciclos por minuto  
 VC prog ml Informe o volume corrente programado em mililitros  
 PIP cmH2O Informe o pico de pressão inspiratória pressão respiratória máxima em cmH2O  
 PEEP cmH2O Informe a pressão expiratória final pulmonar em cmH2O  
 P suporte cmH2O Informe a pressão de suporte em cmH2O  
 Fluxo inspi lmin Informe o fluxo respiratório em litros por minuto  
 T inspi s Informe o tempo respiratório em segundos  
 P acima PEEP cmH2O Informe o limite de pressão acima da pressão expiratória final pulmonar em  
CmH2O  
 TiTe Informe a relação entre o tempo inspiratório e expiratório  
 Sens resp cmH2O Informe o valor de sensibilidade do respirador em cmH2O  
 Tipo de onda Informe o tipo de onda ventilatória  
Após definição dos campos específicos da gasoterapia o usuário deverá informar o modo de administração  
conforme 1º horário se necessário ou a critério médico e em seguida informar a recorrência do item se o item  
deverá ser mantido até 2º ordem na prescrição ou programado Além disso há a possibilidade de incluir um material  
associado à gasoterapia grupo materiais associados Este material poderá ser apresentado conforme regra  
Cadastros gerais  Aplicação principal  Farmácia  Regra de geração de materiais do gás  


4163 Exames e procedimentos  
Os itens apresentados no localizador deste grupo são provenientes da função Exames e procedimentos  
internos Todos os exames e procedimentos da instituição deverão possuir um registro de procedimento  
interno  
Se o procedimento for do tipo controle de glicemia devese definir na função Exames e procedimentos internos  
qual o tipo de controle o procedimento trata No campo Glicemia configurar controle intensivo de glicemia ou  
controle convencional de glicemia  
4164 Nutrição  
41641 Dietas orais  
Este item permite a prescrição de dietas orais onde os registros são provenientes do cadastro de dietas em  
Cadastros gerais  Aplicação principal  Nutrição  Dieta  
41642 Dieta enteral  
Este item permite a prescrição de dietas enterais industrializadas Através do localizador serão apresentados  
produtos provenientes da função Cadastro de materiais com registro de gêneros alimentícios Assim como o  
cadastro de medicamentos e soluções devese realizar o cadastro para os produtos da nutrição dietas enterais e  
suplementos Desta forma ao prescrever o item os campos são automaticamente preenchidos conforme regras  
padrões definidas pela instituição via dose etc  
41643 Suplementos  
Este item permite a prescrição de suplementos nutricionais Através do localizador serão apresentados os produtos  
provenientes da função Cadastro de materiais com registro de gêneros alimentícios Assim como o cadastro de  
medicamentos e soluções devese realizar o cadastro para os produtos da nutrição dietas enterais e suplementos  
Desta forma ao prescrever o item os campos são automaticamente preenchidos conforme regras padrões definidas  
pela instituição via dose etc  
41644 Jejum  
Este item permite a prescrição de jejum para o paciente onde quando programado o usuário poderá definir o  
momento de início data e horário e término do período de jejum  


