# Programa: fluxo.py
# Autor: ChatGPT
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import networkx as nx
import re
from collections import defaultdict, deque

def read_file(filepath):
    """Lê arquivo com encoding apropriado"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='latin1') as f:
                return f.read()
        except Exception as e:
            print(f"Erro ao ler arquivo {filepath}: {e}")
            return ""
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {filepath}")
        return ""
    except Exception as e:
        print(f"Erro inesperado ao ler {filepath}: {e}")
        return ""

def parse_requirements_file(content):
    """Parse do Arquivo 1 - REQUIREMENTS"""
    jobs_requirements = {}
    lines = content.strip().split('\n')
    current_job = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('*'):
            continue
            
        # Verifica se é um job (linha sem espaços no início)
        if not line.startswith(' ') and not line.startswith('JOB='):
            current_job = line[:8].strip()  # Posição 1, tamanho 8
            jobs_requirements[current_job] = []
        elif line.startswith('JOB=') and current_job:
            # Extrai o job dependency (posição 25, tamanho 9)
            job_dep = line.replace('JOB=', '').strip()
            if job_dep.startswith('?'):
                job_dep = job_dep[1:]  # Remove o '?' se existir
            jobs_requirements[current_job].append(job_dep)
    
    return jobs_requirements

def parse_successor_file(content):
    """Parse do Arquivo 2 - SUCCESSOR JOBS"""
    jobs_successors = {}
    lines = content.strip().split('\n')
    current_job = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Verifica se é um job (linha sem muitos espaços no início)
        if not line.startswith('        ') and not line.startswith('JOB='):
            current_job = line[:8].strip()  # Posição 1, tamanho 8
            jobs_successors[current_job] = []
        elif line.startswith('JOB=') and current_job:
            # Extrai o successor job (posição 27, tamanho 9)
            job_succ = line.replace('JOB=', '').strip()
            if job_succ.startswith('?'):
                job_succ = job_succ[1:]  # Remove o '?' se existir
            jobs_successors[current_job].append(job_succ)
    
    return jobs_successors

def create_hierarchical_layout(requirements, successors):
    """Cria um layout hierárquico organizado"""
    
    # Combina todas as dependências
    all_dependencies = {}
    
    # Adiciona requirements (reversed - quem depende de quem)
    for job, deps in requirements.items():
        for dep in deps:
            if dep not in all_dependencies:
                all_dependencies[dep] = []
            all_dependencies[dep].append(job)
    
    # Adiciona successors
    for job, succs in successors.items():
        if job not in all_dependencies:
            all_dependencies[job] = []
        all_dependencies[job].extend(succs)
    
    # Remove duplicatas
    for job in all_dependencies:
        all_dependencies[job] = list(set(all_dependencies[job]))
    
    # Encontra todos os jobs
    all_jobs = set()
    for job, succs in all_dependencies.items():
        all_jobs.add(job)
        all_jobs.update(succs)
    
    # Adiciona jobs sem dependências
    for job in requirements.keys():
        all_jobs.add(job)
    for job in successors.keys():
        all_jobs.add(job)
    
    # Calcula níveis hierárquicos
    levels = {}
    visited = set()
    
    def calculate_level(job, current_level=0):
        if job in visited:
            return levels.get(job, 0)
        
        visited.add(job)
        max_dep_level = -1
        
        # Verifica dependências (jobs que este job precisa)
        job_deps = requirements.get(job, [])
        for dep in job_deps:
            dep_level = calculate_level(dep, current_level + 1)
            max_dep_level = max(max_dep_level, dep_level)
        
        levels[job] = max_dep_level + 1
        return levels[job]
    
    # Calcula níveis para todos os jobs
    for job in all_jobs:
        calculate_level(job)
    
    # Organiza jobs por nível
    jobs_by_level = defaultdict(list)
    for job, level in levels.items():
        jobs_by_level[level].append(job)
    
    return jobs_by_level, all_dependencies

def plot_improved_control_m_style(jobs_by_level, dependencies):
    """Plota o grafo melhorado estilo Control-M"""
    
    # Configurações do gráfico
    fig, ax = plt.subplots(1, 1, figsize=(20, 14))
    
    # Cores para diferentes tipos de jobs
    colors = {
        'start': '#90EE90',      # Verde claro para jobs iniciais
        'middle': '#87CEEB',     # Azul claro para jobs intermediários  
        'end': '#FFB6C1',        # Rosa claro para jobs finais
        'single': '#DDA0DD'      # Roxo claro para jobs isolados
    }
    
    # Calcula posições
    positions = {}
    level_height = 3
    job_width = 2.5
    job_height = 0.8
    
    max_level = max(jobs_by_level.keys()) if jobs_by_level else 0
    
    for level, jobs in jobs_by_level.items():
        y = (max_level - level) * level_height
        jobs_count = len(jobs)
        
        # Centraliza jobs no nível
        total_width = jobs_count * job_width + (jobs_count - 1) * 0.5
        start_x = -total_width / 2
        
        for i, job in enumerate(sorted(jobs)):
            x = start_x + i * (job_width + 0.5) + job_width / 2
            positions[job] = (x, y)
    
    # Desenha conexões primeiro (para ficarem atrás)
    for job, succs in dependencies.items():
        if job in positions:
            for succ in succs:
                if succ in positions:
                    x1, y1 = positions[job]
                    x2, y2 = positions[succ]
                    
                    # Desenha seta curva
                    if abs(x2 - x1) > 0.1:  # Seta curva para conexões distantes
                        mid_x = (x1 + x2) / 2
                        mid_y = min(y1, y2) - 0.3
                        
                        ax.annotate('', xy=(x2, y2 + job_height/2), xytext=(x1, y1 - job_height/2),
                                   arrowprops=dict(arrowstyle='->', lw=1.5, color='#555555',
                                                 connectionstyle="arc3,rad=0.3"))
                    else:  # Seta reta para conexões próximas
                        ax.annotate('', xy=(x2, y2 + job_height/2), xytext=(x1, y1 - job_height/2),
                                   arrowprops=dict(arrowstyle='->', lw=1.5, color='#555555'))
    
    # Desenha os jobs
    for job, (x, y) in positions.items():
        # Determina cor baseada no tipo de job
        has_predecessors = any(job in succs for succs in dependencies.values())
        has_successors = job in dependencies and dependencies[job]
        
        if not has_predecessors and has_successors:
            color = colors['start']
        elif has_predecessors and not has_successors:
            color = colors['end']
        elif has_predecessors and has_successors:
            color = colors['middle']
        else:
            color = colors['single']
        
        # Cria retângulo estilizado
        rect = FancyBboxPatch(
            (x - job_width/2, y - job_height/2), 
            job_width, job_height,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor='#2E4A62',
            linewidth=2,
            alpha=0.9
        )
        ax.add_patch(rect)
        
        # Adiciona texto do job
        ax.text(x, y, job, 
               horizontalalignment='center',
               verticalalignment='center',
               fontsize=9,
               fontweight='bold',
               color='#2E4A62')
    
    # Configurações do gráfico
    ax.set_xlim(-15, 15)
    ax.set_ylim(-2, (max_level + 1) * level_height + 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Título principal
    plt.suptitle('Fluxo de Jobs - Control-M Style', 
                fontsize=18, fontweight='bold', color='#2E4A62', y=0.95)
    
    # Legenda melhorada
    legend_elements = [
        patches.Patch(color=colors['start'], label='Jobs Iniciais'),
        patches.Patch(color=colors['middle'], label='Jobs Intermediários'),
        patches.Patch(color=colors['end'], label='Jobs Finais'),
        patches.Patch(color=colors['single'], label='Jobs Isolados')
    ]
    
    ax.legend(handles=legend_elements, loc='upper right', 
             bbox_to_anchor=(1, 1), fontsize=10)
    
    # Informações adicionais
    total_jobs = len(positions)
    total_connections = sum(len(succs) for succs in dependencies.values())
    
    info_text = f"Total de Jobs: {total_jobs}\nConexões: {total_connections}\nNíveis: {max_level + 1}"
    ax.text(0.02, 0.02, info_text, transform=ax.transAxes, 
           fontsize=11, verticalalignment='bottom',
           bbox=dict(boxstyle="round,pad=0.4", facecolor="#F0F0F0", alpha=0.8))
    
    plt.tight_layout()
    plt.show()

def analyze_dependencies(requirements, successors):
    """Analisa e mostra estatísticas das dependências"""
    print("=" * 50)
    print("           ANÁLISE DE DEPENDÊNCIAS")
    print("=" * 50)
    
    print("\n📋 JOBS COM REQUIREMENTS (dependem de outros):")
    for job, deps in sorted(requirements.items()):
        if deps:
            print(f"   {job:<10} ← {', '.join(deps)}")
    
    print("\n🔄 JOBS COM SUCCESSORS (liberam outros):")
    for job, succs in sorted(successors.items()):
        if succs:
            print(f"   {job:<10} → {', '.join(succs)}")
    
    # Encontra jobs iniciais (sem dependencies)
    all_jobs = set(requirements.keys()) | set(successors.keys())
    for deps in requirements.values():
        all_jobs.update(deps)
    for succs in successors.values():
        all_jobs.update(succs)
    
    jobs_with_deps = {job for job, deps in requirements.items() if deps}
    initial_jobs = all_jobs - jobs_with_deps
    
    print(f"\n🚀 Jobs iniciais (sem dependências): ")
    if initial_jobs:
        for job in sorted(initial_jobs):
            print(f"   • {job}")
    else:
        print("   Nenhum")
    
    # Encontra jobs finais (sem successors)
    jobs_with_succs = {job for job, succs in successors.items() if succs}
    final_jobs = all_jobs - jobs_with_succs
    
    print(f"\n🏁 Jobs finais (sem sucessores): ")
    if final_jobs:
        for job in sorted(final_jobs):
            print(f"   • {job}")
    else:
        print("   Nenhum")
    
    print("\n" + "=" * 50)

def main():
    # Caminhos dos arquivos
    pasta_arquivos = r"C:\Arquivos"
    arquivo_requ = f"{pasta_arquivos}\\REQU.txt"
    arquivo_depj = f"{pasta_arquivos}\\DEPJ.txt"
    
    print("🔍 LENDO ARQUIVOS...")
    print(f"   Requirements: {arquivo_requ}")
    print(f"   Dependencies: {arquivo_depj}")
    
    # Lê os arquivos
    arquivo1_content = read_file(arquivo_requ)
    arquivo2_content = read_file(arquivo_depj)
    
    if not arquivo1_content and not arquivo2_content:
        print("\n❌ ERRO: Nenhum arquivo foi lido com sucesso!")
        print("   Verifique se os arquivos existem na pasta C:\\Arquivos\\")
        return
    
    if not arquivo1_content:
        print("⚠️  AVISO: Arquivo REQU.txt não encontrado. Usando apenas DEPJ.txt")
    
    if not arquivo2_content:
        print("⚠️  AVISO: Arquivo DEPJ.txt não encontrado. Usando apenas REQU.txt")
    
    # Parse dos arquivos
    requirements = parse_requirements_file(arquivo1_content)
    successors = parse_successor_file(arquivo2_content)
    
    # Análise das dependências
    analyze_dependencies(requirements, successors)
    
    # Cria layout hierárquico
    jobs_by_level, dependencies = create_hierarchical_layout(requirements, successors)
    
    total_jobs = sum(len(jobs) for jobs in jobs_by_level.values())
    total_connections = sum(len(succs) for succs in dependencies.values())
    
    print(f"\n📊 ESTATÍSTICAS DO FLUXO:")
    print(f"   Total de jobs: {total_jobs}")
    print(f"   Total de conexões: {total_connections}")
    print(f"   Níveis hierárquicos: {len(jobs_by_level)}")
    
    print(f"\n🎨 Gerando visualização...")
    
    # Plota o gráfico melhorado
    plot_improved_control_m_style(jobs_by_level, dependencies)

if __name__ == "__main__":
    main()