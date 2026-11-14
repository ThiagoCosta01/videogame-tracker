# name: generate_readme.py
# description: Gera o README.md a partir dos arquivos .md em docs/readme_files
# version: 1.1.0
#
# Uso:
#   python generate_readme.py                 # idioma padrão (DEFAULT_LANGUAGE)
#   python generate_readme.py --lang en       # projeto em inglês
#   python generate_readme.py --lang pt       # projeto em português
#   python generate_readme.py --lang auto     # detecta pelo arquivo geral existente
#   python generate_readme.py --debug         # logs detalhados
#
# Códigos de saída: 0 = README gerado | 1 = falha (README não é alterado)

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

# Os caminhos são relativos à pasta DESTE script (não à pasta onde você o executa),
# então funciona de qualquer diretório.
SCRIPT_DIR = Path(__file__).resolve().parent
README_FILE = (SCRIPT_DIR / "../../README.md").resolve()
DOCS_DIR = (SCRIPT_DIR / "../../docs/readme_files").resolve()

# ---> SWITCH DE IDIOMA: "pt", "en" ou "auto"
DEFAULT_LANGUAGE = "auto"  # idioma padrão se não for especificado na linha de comando
FALLBACK_LANGUAGE = "en"  # usado quando "auto" não encontra nenhum arquivo geral

# Tudo o que muda de um idioma para o outro fica aqui.
# Para suportar outro idioma, basta adicionar uma entrada.
LANGUAGES: dict[str, dict[str, str]] = {
    "pt": {
        "general_file": "00-geral.md",
        "summary_title": "📑 Sumário",
    },
    "en": {
        "general_file": "00-overview.md",
        "summary_title": "📑 Summary",
    },
}

logger = logging.getLogger("generate_readme")


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
def setup_logging(debug: bool) -> None:
    """Configura o formato dos logs: hora | nível | função | mensagem."""
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(funcName)-18s | %(message)s",
        datefmt="%H:%M:%S",
        stream=sys.stdout,
    )


# ---------------------------------------------------------------------------
# Idioma
# ---------------------------------------------------------------------------
def detect_language() -> str | None:
    """
    Descobre o idioma olhando qual arquivo geral existe em DOCS_DIR.
    Retorna o código do idioma ou None se nenhum for encontrado.
    """
    logger.info("Detectando idioma em: %s", DOCS_DIR)
    found = []

    for code, config in LANGUAGES.items():
        candidate = DOCS_DIR / config["general_file"]
        exists = candidate.is_file()
        logger.debug("  [%s] %s -> %s", code, candidate, "encontrado" if exists else "ausente")
        if exists:
            found.append(code)

    if not found:
        return None

    if len(found) > 1:
        chosen = DEFAULT_LANGUAGE if DEFAULT_LANGUAGE in found else found[0]
        logger.warning(
            "Arquivos gerais de mais de um idioma encontrados %s; usando '%s'.", found, chosen
        )
        return chosen

    return found[0]


def resolve_language(requested: str) -> str:
    """Converte o valor pedido ('pt', 'en' ou 'auto') em um código de idioma válido."""
    if requested != "auto":
        logger.info("Idioma definido manualmente: '%s'", requested)
        return requested

    detected = detect_language()
    if detected:
        logger.info("Idioma detectado automaticamente: '%s'", detected)
        return detected

    logger.warning(
        "Nenhum arquivo geral encontrado para detectar o idioma; usando '%s'.", FALLBACK_LANGUAGE
    )
    return FALLBACK_LANGUAGE


# ---------------------------------------------------------------------------
# Leitura de arquivos
# ---------------------------------------------------------------------------
def read_text_file(path: Path, purpose: str) -> str:
    """
    Lê um arquivo UTF-8 registrando: caminho completo, se foi encontrado
    e se a leitura deu certo ou errado. Relança a exceção em caso de falha.
    """
    full_path = path.resolve()
    logger.info("Lendo [%s]: %s", purpose, full_path)

    if not full_path.is_file():
        logger.error("Arquivo NÃO encontrado [%s]: %s", purpose, full_path)
        raise FileNotFoundError(full_path)

    logger.debug("Arquivo encontrado (%d bytes)", full_path.stat().st_size)

    try:
        content = full_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        logger.error(
            "Falha na leitura [%s]: %s (%s: %s)", purpose, full_path, type(exc).__name__, exc
        )
        raise

    logger.info("Leitura OK [%s]: %d caracteres", purpose, len(content))
    return content


# ---------------------------------------------------------------------------
# Montagem do README
# ---------------------------------------------------------------------------
def format_title(filename: str) -> str:
    """
    Converte:
        01-arquitetura -> 01 Arquitetura
        banco-de-dados -> Banco De Dados
    """
    return filename.replace("-", " ").title()


def get_general_content(general_file: Path) -> str:
    """Retorna o conteúdo do arquivo geral (introdução) ou '' se ele não existir."""
    logger.info("Procurando arquivo geral: %s", general_file)

    if not general_file.is_file():
        logger.warning("Arquivo geral não encontrado; o README seguirá sem introdução.")
        return ""

    logger.info("Arquivo geral encontrado.")
    return read_text_file(general_file, "geral") + "\n"


def get_markdown_files(general_name: str) -> list[Path]:
    """
    Retorna os arquivos .md de DOCS_DIR, exceto o arquivo geral do idioma ativo,
    em ordem alfabética.
    """
    logger.info("Listando arquivos .md em: %s", DOCS_DIR)

    if not DOCS_DIR.is_dir():
        logger.error("Pasta de documentação NÃO encontrada: %s", DOCS_DIR)
        raise FileNotFoundError(DOCS_DIR)

    other_general_names = {
        config["general_file"]
        for config in LANGUAGES.values()
        if config["general_file"] != general_name
    }

    files: list[Path] = []
    for file in sorted(DOCS_DIR.glob("*.md")):
        if file.name == general_name:
            logger.debug("Ignorado (arquivo geral): %s", file.name)
            continue

        if file.name in other_general_names:
            logger.warning(
                "'%s' parece ser o arquivo geral de outro idioma e será tratado como seção. "
                "Use --lang para trocar o idioma se não for essa a intenção.",
                file.name,
            )

        logger.debug("Incluído: %s", file)
        files.append(file)

    logger.info("%d arquivo(s) de seção encontrado(s).", len(files))
    if not files:
        logger.warning("Nenhuma seção encontrada: o README terá apenas introdução e sumário.")

    return files


def build_summary(files: list[Path], summary_title: str) -> str:
    """Monta o sumário com links para as âncoras de cada seção."""
    logger.info("Montando sumário com %d item(ns).", len(files))

    lines = ["---\n", f"## {summary_title}\n", "\n"]
    for file in files:
        lines.append(f"- [{format_title(file.stem)}](#{file.stem})\n")
    lines.append("\n")

    return "".join(lines)


def build_section(file: Path) -> str:
    """Monta o bloco <details> de uma seção a partir de um arquivo .md."""
    basename = file.stem
    title = format_title(basename)
    logger.info("Processando seção '%s' (%s)", title, file.name)

    content = read_text_file(file, f"seção {basename}")
    if not content.endswith("\n"):
        content += "\n"

    return (
        "\n"
        "---\n"
        f'<a id="{basename}"></a>\n'
        "<details>\n"
        f"  <summary>📌 {title}</summary>\n"
        "\n"
        f"{content}"
        "\n"
        "</details>\n"
    )


def generate_readme(language: str) -> bool:
    """
    Gera o README.md. Todo o conteúdo é montado em memória antes de gravar:
    se qualquer leitura falhar, o README existente não é alterado.
    Retorna True se deu certo e False se falhou.
    """
    config = LANGUAGES[language]
    general_file = DOCS_DIR / config["general_file"]

    logger.info("Idioma ativo: '%s' | arquivo geral: %s", language, config["general_file"])
    logger.info("Pasta de origem : %s", DOCS_DIR)
    logger.info("README de saída : %s", README_FILE)

    try:
        files = get_markdown_files(config["general_file"])

        parts = [
            get_general_content(general_file),
            build_summary(files, config["summary_title"]),
        ]
        parts.extend(build_section(file) for file in files)
    except (OSError, UnicodeDecodeError):
        logger.error("Geração ABORTADA: o README não foi alterado.")
        return False

    try:
        README_FILE.write_text("".join(parts), encoding="utf-8")
    except OSError as exc:
        logger.error("Falha ao gravar %s (%s: %s)", README_FILE, type(exc).__name__, exc)
        return False

    logger.info(
        "README gerado com sucesso: %s (%d seção(ões), %d bytes)",
        README_FILE,
        len(files),
        README_FILE.stat().st_size,
    )
    return True


# ---------------------------------------------------------------------------
# Entrada
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Gera o README.md a partir de docs/readme_files.")
    parser.add_argument(
        "-l",
        "--lang",
        choices=[*LANGUAGES, "auto"],
        default=DEFAULT_LANGUAGE,
        help=f"Idioma do projeto (padrão: {DEFAULT_LANGUAGE}). 'auto' detecta pelo arquivo geral.",
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Mostra logs detalhados.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(args.debug)

    logger.info("Início | script: %s", Path(__file__).resolve())
    language = resolve_language(args.lang)
    ok = generate_readme(language)
    logger.info("Fim | resultado: %s", "SUCESSO" if ok else "FALHA")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())