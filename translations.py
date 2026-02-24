# translations.py

LANGS = {
    "Español": {
        "sidebar_title": "Retail ETL Intelligence",
        "nav_welcome": "📖 Introducción",
        "nav_dashboard": "📊 Dashboard",
        "global_filters": "Filtros Globales",
        "year_range": "Rango de Años",
        "region_filter": "Región",
        "category_filter": "Categoría",
        "download_data": "⬇️ Descargar Datos",
        "developed_by": "Desarrollado por Hely Camargo",
        "hero_title": "📊 Inteligencia Minorista",
        
        # Storytelling Welcome
        "welcome_title": "El Desafío de los Datos",
        "welcome_story_1": "En un mundo donde cada transacción cuenta una historia, una prominente cadena minorista estadounidense se encontraba navegando en un océano de datos no estructurados. Las ventas, los márgenes y los tiempos de envío estaban dispersos en múltiples fuentes, creando un espejismo de información que dificultaba la toma de decisiones estratégicas.",
        "welcome_story_2": "Para revelar la verdad oculta tras las cifras, hemos diseñado este **Centro de Inteligencia (Command Center)**. Nuestro objetivo es transformar el caos en claridad mediante un análisis profundo de tres pilares fundamentales:",
        "welcome_pillar_1_title": "📉 Análisis de Tendencias y Ventas",
        "welcome_pillar_1_desc": "Descubriendo los ritmos estacionales y los productos estrella que impulsan el crecimiento a lo largo del tiempo.",
        "welcome_pillar_2_title": "⚖️ Rentabilidad y Márgenes",
        "welcome_pillar_2_desc": "Identificando fugas de capital y evaluando el impacto real de las políticas de descuento.",
        "welcome_pillar_3_title": "🚚 Eficiencia Operacional",
        "welcome_pillar_3_desc": "Rastreando los tiempos de envío para asegurar la satisfacción del cliente sin comprometer los costos logísticos.",
        "welcome_cta": "Navega a la sección **Dashboard** para explorar los datos en tiempo real.",
        
        "kpi_revenue": "Total Ingresos",
        "kpi_margin": "Margen Promedio",
        "kpi_orders": "Total Órdenes",
        "kpi_shipping": "Días Prom. Envío",
        "tab_sales": "📊 Análisis de Ventas",
        "tab_profit": "💰 Rentabilidad",
        "tab_ops": "🚚 Operaciones",
        "tab_conclusions": "📋 Conclusiones",
        
        # Tab 1
        "sales_yoy_title": "Ventas Mes a Mes (YoY)",
        "sales_region_title": "Rentabilidad por Región",
        "sales_category_title": "Ventas por Categoría y Sub-categoría",
        "sales_insight": "💡 **La Historia de las Ventas:** A lo largo de los años, observamos un patrón innegable: los consumidores esperan hasta el Q4 para las mayores inversiones, impulsados por los Black Fridays navideños. Categorías pesadas como *Tecnología* y *Mobiliario* son los héroes indiscutibles. **Recomendación:** Aumentar inventario tecnológico un mes antes del Q4.",
        
        # Tab 2
        "profit_heatmap_title": "Margen de Beneficio: Categoría vs Trimestre",
        "profit_scatter_title": "Descuento vs Margen de Beneficio",
        "profit_bar_title": "Top 10 Sub-categorías: Más y Menos Rentables",
        "profit_insight": "💡 **Alerta de Rentabilidad:** La fiebre de los decuentos está desangrando áreas críticas. Al analizar en detalle, descubrimos que otorgar descuentos superiores al 40% en *Mesas* y *Libreros* no impulsa retención real, sino que garantiza pérdidas sistemáticas. **Recomendación:** Limitar el techo de descuento de mobiliario a 20%.",
        
        # Tab 3
        "ops_box_title": "Días de Envío por Modo",
        "ops_geo_title": "Ingresos Totales por Estado",
        "ops_timeline_title": "Volumen de Órdenes Semanal",
        "ops_insight": "💡 **El Termómetro Operativo:** Promediar 5 días en envíos de clase estándar parece razonable desde la logística general; sin embargo, en regiones de máxima demanda como las costas (California y N. York), este tiempo de espera mina la lealtad del cliente B2B. **Recomendación:** Considerar *Micro-hubs* de despacho para atenuar los tiempos pico.",
        
        # Tab 4
        "conclusions_title": "Resumen Ejecutivo",
        "conc_f1_title": "🛋️ Fuga de Capital en Mobiliario",
        "conc_f1_finding": "La categoría de mobiliario, específicamente Mesas y Libreros, presenta pérdidas sistémicas debido a campañas de descuento agresivas que frecuentemente superan el 40%.",
        "conc_f1_impact": "Esta política erosiona el margen neto hasta un -25% en estos productos, arrastrando significativamente la rentabilidad trimestral global de la empresa.",
        "conc_f1_action": "Implementar un techo estricto del 20% para los descuentos en la categoría de mobiliario pesado. (Prioridad: Alta 🔴)",
        "conc_f1_prediction": "Al contener esta erosión, proyectamos una recuperación del margen de beneficio al 12% para el próximo semestre, sacrificando menos del 5% del volumen de ventas.",
        
        "conc_f2_title": "📆 La Dependencia del Q4",
        "conc_f2_finding": "Existe un ciclo de compra marcadamente estacional donde el cuarto trimestre (Q4) concentra los mayores picos de ventas año tras año, impulsado por Tecnología.",
        "conc_f2_impact": "Genera estrés en la cadena de suministro y crea cuellos de botella en el flujo de caja durante los tres primeros trimestres del año.",
        "conc_f2_action": "Adelantar las campañas de marketing corporativo al Q3 y asegurar inventario tecnológico con 3 meses de anticipación. (Prioridad: Media 🟡)",
        "conc_f2_prediction": "Una distribución de ventas más equilibrada reducirá los costos de almacenamiento de emergencia y suavizará la curva anual de ingresos.",
        
        "conc_f3_title": "🚚 El Cuello de Botella Costero",
        "conc_f3_finding": "Los envíos de clase estándar promedian 5.5 días. Aunque es aceptable a nivel nacional, resulta crítico en estados costeros de alta demanda como California y Nueva York.",
        "conc_f3_impact": "Tiempos logísticos prolongados socavan la retención del cliente B2B y aumentan las quejas por cumplimiento de plazos.",
        "conc_f3_action": "Desplegar centros de distribución regionales (Micro-hubs) dedicados a las costas Este y Oeste. (Prioridad: Alta 🔴)",
        "conc_f3_prediction": "Se estima una reducción del tiempo promedio de envío a 2.5 días en zonas críticas, incrementando la lealtad del cliente corporativo en un 15%."
    },
    "English": {
        "sidebar_title": "Retail ETL Intelligence",
        "nav_welcome": "📖 Introduction",
        "nav_dashboard": "📊 Dashboard",
        "global_filters": "Global Filters",
        "year_range": "Year Range",
        "region_filter": "Region",
        "category_filter": "Category",
        "download_data": "⬇️ Download Data",
        "developed_by": "Developed by Hely Camargo",
        "hero_title": "📊 Retail Intelligence",
        
        # Storytelling Welcome
        "welcome_title": "The Data Challenge",
        "welcome_story_1": "In a world where every transaction tells a story, a prominent US retail chain found itself navigating an ocean of unstructured data. Sales, margins, and shipping times were scattered across multiple sources, creating a mirage of information that hindered strategic decision-making.",
        "welcome_story_2": "To reveal the hidden truth behind the numbers, we have designed this **Intelligence Center (Command Center)**. Our goal is to transform chaos into clarity through an in-depth analysis of three fundamental pillars:",
        "welcome_pillar_1_title": "📉 Sales & Trends Analysis",
        "welcome_pillar_1_desc": "Discovering the seasonal rhythms and star products that drive growth over time.",
        "welcome_pillar_2_title": "⚖️ Profitability & Margins",
        "welcome_pillar_2_desc": "Identifying capital leaks and evaluating the true impact of discount policies.",
        "welcome_pillar_3_title": "🚚 Operational Efficiency",
        "welcome_pillar_3_desc": "Tracking shipping times to ensure customer satisfaction without compromising logistics costs.",
        "welcome_cta": "Navigate to the **Dashboard** section to explore the data in real-time.",
        
        "kpi_revenue": "Total Revenue",
        "kpi_margin": "Avg Profit Margin",
        "kpi_orders": "Total Orders",
        "kpi_shipping": "Avg Shipping Days",
        "tab_sales": "📊 Sales Analysis",
        "tab_profit": "💰 Profitability",
        "tab_ops": "🚚 Operations",
        "tab_conclusions": "📋 Conclusions",
        
        # Tab 1
        "sales_yoy_title": "Month-over-Month Sales (YoY)",
        "sales_region_title": "Profitability by Region",
        "sales_category_title": "Sales by Category & Sub-category",
        "sales_insight": "💡 **The Story of Sales:** Over the years, we've observed an undeniable pattern: consumers wait until Q4 for major investments, driven by holiday Black Fridays. Heavyweight categories like *Technology* and *Furniture* are the undisputed heroes. **Recommendation:** Increase technology inventory one month prior to Q4.",
        
        # Tab 2
        "profit_heatmap_title": "Profit Margin: Category vs Quarter",
        "profit_scatter_title": "Discount vs Profit Margin",
        "profit_bar_title": "Top 10 Sub-categories: Most & Least Profitable",
        "profit_insight": "💡 **Profitability Alert:** The discount fever is bleeding critical areas. Upon closer look, we discovered that granting discounts over 40% on *Tables* and *Bookcases* doesn't drive true retention; it guarantees systematic losses. **Recommendation:** Cap furniture discounts at a strict 20%.",
        
        # Tab 3
        "ops_box_title": "Shipping Days by Mode",
        "ops_geo_title": "Total Revenue by State",
        "ops_timeline_title": "Weekly Order Volume",
        "ops_insight": "💡 **The Operational Thermometer:** Averaging 5 days for standard shipping seems reasonable from a general logistics standpoint; however, in high-demand coastal regions (California & NY), this wait time undermines B2B customer loyalty. **Recommendation:** Consider *Micro-hubs* to mitigate peak delivery times.",
        
        # Tab 4
        "conclusions_title": "Executive Summary",
        "conc_f1_title": "🛋️ Furniture Capital Bleed",
        "conc_f1_finding": "The furniture category, specifically Tables and Bookcases, shows systemic losses due to aggressive discount campaigns frequently exceeding 40%.",
        "conc_f1_impact": "This policy erodes net margins to -25% on these products, significantly dragging down the company's overall quarterly profitability.",
        "conc_f1_action": "Implement a strict 20% cap on discounts for the heavy furniture category. (Priority: High 🔴)",
        "conc_f1_prediction": "By containing this erosion, we project a profit margin recovery to 12% by next semester, sacrificing less than 5% of sales volume.",
        
        "conc_f2_title": "📆 The Q4 Dependency",
        "conc_f2_finding": "There is a strongly seasonal purchasing cycle where the fourth quarter (Q4) continually concentrates the highest sales peaks, driven by Technology.",
        "conc_f2_impact": "This causes supply chain stress and cash flow bottlenecks during the first three quarters of the year.",
        "conc_f2_action": "Launch corporate marketing campaigns earlier in Q3 and secure tech inventory 3 months in advance. (Priority: Medium 🟡)",
        "conc_f2_prediction": "A more balanced sales distribution will reduce emergency warehousing costs and smooth out the annual revenue curve.",
        
        "conc_f3_title": "🚚 The Coastal Bottleneck",
        "conc_f3_finding": "Standard class shipments average 5.5 days. While nationally acceptable, this is highly critical in high-demand coastal states like California and New York.",
        "conc_f3_impact": "Prolonged logistics times undermine B2B customer retention and increase complaints regarding delivery deadlines.",
        "conc_f3_action": "Deploy dedicated regional distribution micro-hubs for the East and West coasts. (Priority: High 🔴)",
        "conc_f3_prediction": "Average shipping times in critical zones are estimated to drop to 2.5 days, boosting corporate customer loyalty by 15%."
    },
    "Português": {
        "sidebar_title": "Inteligência de Varejo ETL",
        "nav_welcome": "📖 Introdução",
        "nav_dashboard": "📊 Dashboard",
        "global_filters": "Filtros Globais",
        "year_range": "Intervalo de Anos",
        "region_filter": "Região",
        "category_filter": "Categoria",
        "download_data": "⬇️ Baixar Dados",
        "developed_by": "Desenvolvido por Hely Camargo",
        "hero_title": "📊 Inteligência de Varejo",
        
        # Storytelling Welcome
        "welcome_title": "O Desafio dos Dados",
        "welcome_story_1": "Em um mundo onde cada transação conta uma história, uma proeminente rede de varejo dos EUA viu-se navegando em um oceano de dados não estruturados. Vendas, margens e tempos de envio estavam dispersos em várias fontes, criando uma miragem de informações que dificultava a tomada de decisões estratégicas.",
        "welcome_story_2": "Para revelar a verdade oculta por trás dos números, projetamos este **Centro de Inteligência (Command Center)**. Nosso objetivo é transformar o caos em clareza através de uma análise aprofundada de três pilares fundamentais:",
        "welcome_pillar_1_title": "📉 Análise de Vendas e Tendências",
        "welcome_pillar_1_desc": "Descobrindo os ritmos sazonais e os produtos estrela que impulsionam o crescimento ao longo do tempo.",
        "welcome_pillar_2_title": "⚖️ Lucratividade e Margens",
        "welcome_pillar_2_desc": "Identificando vazamentos de capital e avaliando o verdadeiro impacto das políticas de desconto.",
        "welcome_pillar_3_title": "🚚 Eficiência Operacional",
        "welcome_pillar_3_desc": "Rastreando tempos de envio para garantir a satisfação do cliente sem comprometer os custos logísticos.",
        "welcome_cta": "Navegue até a seção **Dashboard** para explorar os dados em tempo real.",
        
        "kpi_revenue": "Receita Total",
        "kpi_margin": "Margem Média",
        "kpi_orders": "Total de Pedidos",
        "kpi_shipping": "Dias Méd. Envio",
        "tab_sales": "📊 Análise de Vendas",
        "tab_profit": "💰 Lucratividade",
        "tab_ops": "🚚 Operações",
        "tab_conclusions": "📋 Conclusões",
        
        # Tab 1
        "sales_yoy_title": "Vendas Mês a Mês (YoY)",
        "sales_region_title": "Lucratividade por Região",
        "sales_category_title": "Vendas por Categoria e Subcategoria",
        "sales_insight": "💡 **A História das Vendas:** Ao longo dos anos, observamos um padrão inegável: os consumidores aguardam até o Q4 para os maiores investimentos, impulsionados pelos Black Fridays de fim de ano. Categorias de peso como *Tecnologia* e *Móveis* são as grandes heroínas. **Recomendação:** Aumentar o estoque de tecnologia um mês antes do Q4.",
        
        # Tab 2
        "profit_heatmap_title": "Margem de Lucro: Categoria vs Trimestre",
        "profit_scatter_title": "Desconto vs Margem de Lucro",
        "profit_bar_title": "Top 10 Subcategorias: Mais e Menos Lucrativas",
        "profit_insight": "💡 **Alerta de Lucratividade:** A febre dos descontos está sangrando áreas críticas. Ao analisar de perto, descobrimos que conceder descontos superiores a 40% em *Mesas* e *Estantes* não gera retenção real, mas garante perdas sistemáticas. **Recomendação:** Limitar o teto de desconto de móveis a 20%.",
        
        # Tab 3
        "ops_box_title": "Dias de Envio por Modo",
        "ops_geo_title": "Receita Total por Estado",
        "ops_timeline_title": "Volume de Pedidos Semanal",
        "ops_insight": "💡 **O Termômetro Operacional:** Ter uma média de 5 dias em envios de classe padrão parece razoável em termos gerais; no entanto, em regiões de alta demanda nas costas (Califórnia e NY), esse tempo de espera mina a lealdade do cliente B2B. **Recomendação:** Considerar *Micro-hubs* de despacho para atenuar tempos de pico.",
        
        # Tab 4
        "conclusions_title": "Resumo Executivo",
        "conc_f1_title": "🛋️ Fuga de Capital em Móveis",
        "conc_f1_finding": "A categoria de móveis, especificamente Mesas e Estantes, apresenta perdas sistêmicas devido a campanhas de desconto agressivas que frequentemente ultrapassam 40%.",
        "conc_f1_impact": "Esta política corrói a margem líquida até -25% nestes produtos, arrastando significativamente a rentabilidade trimestral global da empresa.",
        "conc_f1_action": "Implementar um teto estrito de 20% para os descontos na categoria de móveis. (Prioridade: Alta 🔴)",
        "conc_f1_prediction": "Ao conter esta erosão, projetamos uma recuperação da margem de lucro para 12% no próximo semestre, sacrificando menos de 5% do volume de vendas.",
        
        "conc_f2_title": "📆 A Dependência do Q4",
        "conc_f2_finding": "Existe um ciclo de compra fortemente sazonal onde o quarto trimestre (Q4) concentra os maiores picos de vendas ano após ano, impulsionado por Tecnologia.",
        "conc_f2_impact": "Isso causa estresse na cadeia de suprimentos e cria gargalos no fluxo de caixa durante os três primeiros trimestres do ano.",
        "conc_f2_action": "Antecipar as campanhas de marketing corporativo para o Q3 e garantir o estoque tecnológico com 3 meses de antecedência. (Prioridade: Média 🟡)",
        "conc_f2_prediction": "Uma distribuição de vendas mais equilibrada reduzirá os custos de armazenamento de emergência e suavizará a curva anual de receita.",
        
        "conc_f3_title": "🚚 O Gargalo Costeiro",
        "conc_f3_finding": "Os envios de classe padrão levam em média 5.5 dias. Embora seja aceitável nacionalmente, isso é crítico em estados costeiros de alta demanda como Califórnia e Nova York.",
        "conc_f3_impact": "Tempos logísticos prolongados minam a retenção de clientes B2B e aumentam as reclamações sobre prazos de entrega.",
        "conc_f3_action": "Implantar micro-hubs de distribuição regional dedicados às costas Leste e Oeste. (Prioridade: Alta 🔴)",
        "conc_f3_prediction": "Estima-se que o tempo médio de envio caia para 2.5 dias em zonas críticas, aumentando a fidelidade do cliente corporativo em 15%."
    }
}
