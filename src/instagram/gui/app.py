import streamlit as st

class RelatoriosGenUI:

    def report_generation(self):
         if st.session_state.generating:
              st.session_state.report = self.generate_report
              (
                   st.session_state.instagram_description, st.session_state.
                   topic_of_the_week
              )

    def sidebar(self):
        with st.sidebar:    
                st.title("Relatórios Programação Instagram")
                        
                st.write(
                    """
                    Para gerar os relatórios , escreva a descrição da página e o tópico. 
                    \n
                    O time de Agentes de IA irá gerar os relatórios para você!
                    """
                )

                st.text_input(
                     "Descrição do Instagram", 
                     key="instagram_description", 
                     placeholder="Nutrição"
                )

                st.text_input(
                     "Tópico da semana",
                     key="topic_of_the_week",
                     placeholder="Dieta para perder peso",
                )

                if st.button("Gerar relatórios"):
                     st.session_state.generating = True


    def render(self):
        st.set_page_config(page_title="Relatórios Programação Instagram", page_icon="📝")

        if "topic" not in st.session_state:
             st.session_state.topic = ""
        
        if "personal_message" not in st.session_state:
             st.session_state.personal_messagep = ""

        if "newsletter" not in st.session_state:
             st.session_state.newsletter = ""

        if "generating" not in st.session_state:
             st.session_state.newsletter = False

        

        self.sidebar()
 

if __name__ == "__main__":
    RelatoriosGenUI().render()