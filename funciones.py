import streamlit as st
import streamlit.components.v1 as components

def styles(route):
    with open(route) as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)

def fuentes():
    return st.markdown("""
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz@0,9..40;1,9..40&display=swap" rel="stylesheet">
        </head>
    """, unsafe_allow_html=True)


def header():
    return """
        <div id="header" class="d-flex justify-content-end align-items-center pe-2 pt-2">
            <div class="link-div fs-4 me-3" style="font-family: 'DM Sans', 'Source Sans Pro'", sans-serif;"><a class="header-link" href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app/Asistente_Musical" target="_self">Asistente Musical</a></div>
            <div class="link-div fs-4 me-3" style="font-family: 'DM Sans', 'Source Sans Pro'", sans-serif;"><a class="header-link" href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app/Reconocimiento_Facial" target="_self">Reconocimiento facial</a></div>
            <div class="link-div fs-4 me-3" style="font-family: 'DM Sans', 'Source Sans Pro'", sans-serif;"><a class="header-link" href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app/Chatbot" target="_self">Chatbot</a></div>
            <div class="link-div fs-4" style="font-family: 'DM Sans', 'Source Sans Pro'", sans-serif;"><a class="header-link" href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app/Sobre_Nosotros" target="_self">Sobre nosotros</a></div>
        </div>
    """

def header2():
    return """
        <div id="header" class="d-flex justify-content-end align-items-center pe-2 pt-2">
            <div class="logo">
                <a href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app"><img src="https://beatbuddyapp.streamlit.app:443/~/+/media/cdf0488c738115d7f79bedc0dbba33fcddaf432f3e57a3d5eea75553.png" alt="Logo"></a>
            </div>
            <div class="link-div fs-4 me-3" style="font-family: 'DM Sans', 'Source Sans Pro'", sans-serif;"><a class="header-link" href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app/Asistente_Musical" target="_self">Asistente Musical</a></div>
            <div class="link-div fs-4 me-3" style="font-family: 'DM Sans', 'Source Sans Pro'", sans-serif;"><a class="header-link" href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app/Reconocimiento_Facial" target="_self">Reconocimiento facial</a></div>
            <div class="link-div fs-4 me-3" style="font-family: 'DM Sans', 'Source Sans Pro'", sans-serif;"><a class="header-link" href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app/Chatbot" target="_self">Chatbot</a></div>
            <div class="link-div fs-4" style="font-family: 'DM Sans', 'Source Sans Pro'", sans-serif;"><a class="header-link" href="https://prueba-ywxahkhd6pvxdonrqv3wse.streamlit.app/Sobre_nosotros" target="_self">Sobre nosotros</a></div>
        </div>
    """


def home():
    with open("./src/js/anime.min.js", "r") as f:
        animejs = f.read()

    css = """
        @import url('https://fonts.googleapis.com/css2?family=Francois+One&display=swap');
        .francois-one-regular {
            font-family: "Francois One", sans-serif;
            font-weight: 400;
            font-size: 2.75em;
            font-style: normal;
        }
        .dm-sans-4 {
            font-family: "DM Sans", sans-serif;
            font-optical-sizing: auto;
            font-size: 1.5em;
            font-weight: 400;
            font-style: normal;
        }
        body {
            display: flex;
            justify-content: center;
            align-content: center;
        }
        #inicio-body {
            width: 100%;
            height: 100%;
            margin: auto;
            display: flex;
            justify-content: space-evenly;
            align-content: center;
            margin-top: 3rem;
        }
        #img-container {
            width: 50%;
            height: 75%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #inicio-img {
            max-width: 400px;
            min-width: 300px;
        }
        #inicio-beatbuddy {
            width: 50%;
            padding-top: 3%;
            padding-bottom: 3%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
        }
        #inicio-titulo {
            width: 75%;
            text-align: center;
            color: #FFFFFF;
            font-family: "Francois One", sans-serif;
            font-weight: 400;
            font-size: 2.75em;
            font-style: normal;
        }
        #inicio-descrip {
            width: 75%;
            text-align: center;
            color: #FFFFFF;
        }
        #btn-empezar {
            width: 37%;
            background-color: #9062a6;
            color: #FFFFFF;
            text-decoration: none;
            text-align: center;
            padding: 1rem 3rem 1rem 3rem;
            border-radius: 0.375rem;
            box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
        }
        .ml6 {
            position: relative;
            font-weight: 900;
        }
        .ml6 .text-wrapper {
            position: relative;
            display: inline-block;
            overflow: hidden;
        }
        .ml6 .letter {
            display: inline-block;
            line-height: 1em;
        }
    """

    my_js = """
        document.addEventListener("DOMContentLoaded", function() {
            var inicio_titulo = document.getElementById("inicio-titulo");
            var inicio_descrip = document.getElementById("inicio-descrip");

            var textWrapper = document.querySelector('.ml6 .letters');
            textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

            anime.timeline()
                .add({
                    targets: '.ml6 .letter',
                    translateY: ["1.5em", 0],
                    translateZ: 0,
                    duration: 750,
                    delay: (el, i) => 50 * i
                }).add({
                    targets: inicio_descrip,
                    scale: [0, 1],
                    opacity: [0, 1],
                    easing: 'easeOutElastic(1, .5)',
                    duration: 1000,
                    delay: 500
                });
            });
    """

    my_html = f"""
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz@0,9..40;1,9..40&display=swap" rel="stylesheet">
            <style>{css}</style>
        </head>
        <div id="inicio-body">
            <div id="img-container">
                <img id="inicio-img" src="https://beatbuddyapp.streamlit.app:443/~/+/media/cdf0488c738115d7f79bedc0dbba33fcddaf432f3e57a3d5eea75553.png" alt="BeatBuddy"/>
            </div>
            <div id="inicio-beatbuddy">
                <div id="inicio-titulo" class="francois-one-regular ml6">
                    <span class="text-wrapper">
                        <span class="letters">Lorem Ipsum dolor</span>
                    </span>
                </div>
                <div id="inicio-descrip" class="dm-sans-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut semper, felis et elementum efficitur, velit ipsum congue tellus, sit amet placerat massa tellus at sem. </div>
                <a id="btn-empezar" class="dm-sans-4" href="https://beatbuddyapp.streamlit.app/Asistente_Musical">¡Empieza aquí!</a>
            </div>
        </div>
        <script>{animejs}</script>
        <script>{my_js}</script>
        """

    return my_html

    
def asistente_musical():
    return f"""
        <div id="asistente-body" class="d-flex flex-column text-white">
            <div id="bloque1" class="w-50 d-flex flex-column align-items-center">
                <span class="text-center fs-2">Pregunta 1</span>
                <div class="">
                    <div class="w-100 fs-4">Triste</div>
                    <div class="w-100 fs-4">Feliz</div>
                </div>
            </div>
            {st.divider()}
            <div id="bloque2" class="w-50 d-flex flex-column align-items-center">
                <span class="text-center fs-2">Pregunta 2</span>
                <div class="">
                    <div class="w-100 fs-4">Triste</div>
                    <div class="w-100 fs-4">Feliz</div>
                </div>
            </div>
        </div>
    """

def reconocimiento():
    return f"""
        <div id="recog-body" class="d-flex justify-content-evenly align-items-center mt-5 px-5">
            <div id="inicio-beatbuddy" class="w-75 h-25 d-flex flex-column justify-content-evenly align-items-center">
                <div class="w-200 fs-2 text-center text-white" style="font-family: 'DM Sans', 'Source Sans Pro'"><b>Reconocimiento facial</b></div>
                <div id="inicio-texto" class="w-75 fs-5 text-center text-white" style="font-family: 'DM Sans', 'Source Sans Pro'">Sube una imagen o toma una foto con tu cámara para que el programa identifique tu emoción y escoja una canción acorde a tu sentimiento.</div>
            </div>
        </div>
    """

def prediccion(predicted_emotion):
    return f"""
        <div id="inicio-beatbuddy" class="w-200 h-3 d-flex flex-column justify-content-evenly align-items-center">
            <div class="w-200 fs-4 text-center text-white">Parece ser que estás:<b> {predicted_emotion.upper()}</b></div>
            <div class="w-200 fs-1 text-center text-white"><b>TU CANCIÓN IDEAL ES...</b></div>
        </div>
    """


def sobre_nosotros():
    return f"""
        <div id="about-us" class="d-flex justify-content-around align-items-center">
            <div id="about-us-descrip" class="h-75 d-flex align-items-center">
                <span class="text-white fs-4 dm-sans-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut semper, felis et elementum efficitur, velit ipsum congue tellus, sit amet placerat massa tellus at sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut semper, felis et elementum efficitur, velit ipsum congue tellus, sit amet placerat massa tellus at sem.  </span>
            </div>
            <div class="w-25 h-50 d-flex flex-column justify-content-around align-items-center">
                <div id="linkedin-div" class="d-flex flex-column justify-content-start">
                    <div class="d-flex align-items-center">
                        <img id="linkedin-img" src="https://beatbuddyapp.streamlit.app:443/~/+/media/ff9bf60bd47e2d8590057ce1913f1eb466c7a4b458d2d78fd7a18c8c.png" alt="Linkedin"/>
                        <span class="text-white fs-4 ps-1">Linkedin</span>
                    </div>
                    <a class="about-us-links fs-5 ps-1 pt-1" href="https://www.linkedin.com/in/itsupportspecialist-sysadmin-christianmd/">Christian Martín Díaz</a>
                    <a class="about-us-links fs-5 ps-1 pt-1" href="https://www.linkedin.com/in/maria-eugeniasanchez/">María Eugenia Sánchez Sánchez</a>
                    <a class="about-us-links fs-5 ps-1 pt-1" href="https://www.linkedin.com/in/pablo-mart%C3%ADn-trujillo/">Pablo Martín Trujillo</a>
                </div>
                <div id="github-div" class="d-flex flex-column justify-content-start">
                    <div class="d-flex align-items-center">
                        <img id="github-img" src="https://beatbuddyapp.streamlit.app:443/~/+/media/d96c7815c16b6bb69483387073e3a78b19728b28d57e1d916101759e.png" alt="Github"/>
                        <span class="text-white fs-4 ps-1">Github</span>
                    </div>
                    <a class="about-us-links fs-5 ps-1 pt-1" href="https://github.com/chrismartindiaz">Christian Martín Díaz</a>
                    <a class="about-us-links fs-5 ps-1 pt-1" href="https://github.com/mariasnchez">María Eugenia Sánchez Sánchez</a>
                    <a class="about-us-links fs-5 ps-1 pt-1" href="https://github.com/martintpablo">Pablo Martín Trujillo</a>
                </div>
            </div>
        </div>
    """


