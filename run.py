import asyncio
import os
import sys

from browser_use import Agent, BrowserConfig, Browser
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from report.reporte import generate_reporte

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró GEMINI_API_KEY en las variables de entorno")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(api_key))

# Create agent with the model
browser = Browser(
    config=BrowserConfig(
        headless=True,                                 # Modo Headless  
        disable_security=True,
#        chrome_instance_path="/usr/bin/google-chrome", # Uso de navegador Local, Si no se espeficica usa el de playwright
#        chrome_instance_path="/usr/bin/brave-browser", # Uso de navegador Local, Si no se espeficica usa el de playwright
    )
)

context = BrowserContext(
    browser=browser,
    config=BrowserContextConfig(
        browser_window_size={'width': 1360, 'height': 700},
        highlight_elements=True,
        viewport_expansion=500,
        save_recording_path="./report/videos_result",
        no_viewport=False

    )
)


prompt = """
 Ingresa google.com.pe y busca browser-use y valida la ultima version estable
"""


async def main():
    try:

        agent = Agent(
            task=prompt,
            llm=llm,
            use_vision=True,  # Enable vision capabilities
            browser_context=context,

        )
        ruta = './report/result/report.json'
        history = await agent.run()
        history.save_to_file(ruta)
        generate_reporte(ruta)

        if history.has_errors():
            print("Execution completed with errors")
            return 1  # Indica error
        
        print("Execution completed successfully")
        return 0  # Indica éxito

    except Exception as e:
        print(f"Error during execution: {e}")
        return 1  # Indica error

    finally:
        await context.close()
        await browser.close()  # Ensure browser is properly closed


if __name__ == '__main__':
    try:
        exit_code = asyncio.run(main())
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit_code = 1
    sys.exit(exit_code)
