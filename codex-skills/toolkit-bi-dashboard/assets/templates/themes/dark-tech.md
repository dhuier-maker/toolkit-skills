# BI 大屏多主题模板

> 适用于智慧城市、乡村、社区、党建、生态、经济、数字孪生等场景的 BI 大屏主题系统。
> 支持 6 套主题，通过 CSS 变量 + 主题配置文件一键切换。
> 触发词：深蓝科技、青绿生态、党建红金、暖橙数据、紫蓝深邃、浅色商务、科技感大屏、智慧大屏、数据大屏、BI大屏主题

---

## 一、主题配置文件 (themes/index.js)

```javascript
/**
 * BI 大屏主题配置系统
 * 支持 6 套主题：深蓝科技、青绿生态、党建红金、暖橙数据、紫蓝深邃、浅色商务
 * 通过 CSS 变量 + 主题 Token 驱动，一键切换
 */

export const themes = {
  // ========== 深蓝科技风（默认） ==========
  techBlue: {
    key: 'techBlue',
    cssKey: 'tech-blue',
    name: '深蓝科技',
    nameEn: 'Tech Blue',
    description: '适用于智慧城市、乡村、社区、态势感知、综合监控',
    aliases: ['darkTech'], // 向后兼容旧键名

    colors: {
      // 背景色
      bgPage: '#0A0E27',
      bgPanel: 'rgba(6, 30, 93, 0.8)',
      bgPanelSolid: '#0C1A3A',
      bgCard: 'rgba(0, 20, 40, 0.5)',

      // 主强调色
      primary: '#00D4FF',
      primaryRgb: '0, 212, 255',
      secondary: '#0088FF',
      accent: '#44FFAA',

      // 状态色
      success: '#44FFAA',
      warning: '#FFD93D',
      danger: '#FF6B6B',
      info: '#0088FF',

      // 文字色
      titleColor: '#FFFFFF',
      panelTitleColor: '#00D4FF',
      textPrimary: '#E0E8FF',
      textMuted: '#6B7FA3',
      highlightColor: '#FFD93D',

      // 边框色
      borderPanel: 'rgba(0, 212, 255, 0.3)',
      borderGlow: 'rgba(0, 212, 255, 0.6)',

      // 图表色板（8色）
      chartColors: ['#00D4FF', '#0088FF', '#FF6B6B', '#FFD93D', '#44FFAA', '#A855F7', '#FF8C42', '#FF69B4'],
    },

    gradients: {
      primary: 'linear-gradient(to top, #003B7A, #00D4FF)',
      secondary: 'linear-gradient(to top, #003088, #0088FF)',
      area: 'linear-gradient(to bottom, rgba(0,212,255,0.3), transparent)',
      panel: 'linear-gradient(180deg, rgba(6,30,93,0.9), rgba(2,12,50,0.9))',
      glowBar: 'linear-gradient(90deg, transparent, #00D4FF, transparent)',
    },

    decoration: {
      cornerStyle: 'tech',          // 科技角标
      headerStyle: 'dotMatrix',     // 点阵纹理标题
      glowEffect: true,             // 光效
      particleEffect: true,         // 粒子效果
      flylineEffect: true,          // 飞线效果
    },

    animation: {
      intensity: 'strong',          // 动效强度：strong / medium / light / minimal
      breathe: true,
      scanLine: true,
    },

    map: {
      areaColor: '#0a2a4a',
      borderColor: '#00D4FF',
      borderWidth: 1,
      emphasisAreaColor: '#1a4a7a',
      emphasisBorderColor: '#FFD93D',
    },

    chart: {
      backgroundColor: 'transparent',
      textColor: '#E0E8FF',
      axisLineColor: 'rgba(0, 212, 255, 0.3)',
      splitLineColor: 'rgba(0, 212, 255, 0.1)',
      axisLabelColor: '#6B7FA3',
    },

    font: {
      title: "'Source Han Sans CN', 'Alibaba-PuHuiTi-Bold', 'Microsoft YaHei Bold', sans-serif",
      data: "'DIN Alternate', 'Roboto-Bold', 'Helvetica Bold', sans-serif",
      body: "'Microsoft YaHei', 'PingFang SC', 'SimHei', sans-serif",
    },

    // 按钮配置
    button: {
      primaryBg: 'linear-gradient(135deg, #0088FF, #00D4FF)',
      primaryText: '#FFFFFF',
      secondaryText: '#00D4FF',
      secondaryBorder: 'rgba(0, 212, 255, 0.5)',
      dangerBg: 'linear-gradient(135deg, #CC3333, #FF6B6B)',
      hoverOverlay: 'rgba(255, 255, 255, 0.15)',
      activeOverlay: 'rgba(0, 0, 0, 0.1)',
      disabledBg: 'rgba(255, 255, 255, 0.1)',
      disabledText: 'rgba(255, 255, 255, 0.3)',
    },

    // Tab 切换配置
    tab: {
      capsuleBg: 'rgba(0, 212, 255, 0.08)',
      activeBg: 'linear-gradient(135deg, #0088FF, #00D4FF)',
    },

    // 标题栏配置
    titleBar: {
      bgTitleBar: 'rgba(0, 212, 255, 0.15)',
      gradientHeaderBg: 'linear-gradient(180deg, rgba(0,212,255,0.12), transparent)',
      gradientHeaderGlow: 'linear-gradient(90deg, transparent, #00D4FF, transparent)',
      gradientTitleText: 'linear-gradient(90deg, #00D4FF, #FFFFFF 50%, #00D4FF)',
      gradientPanelTitleText: 'linear-gradient(90deg, #00D4FF, #FFFFFF)',
    },

    shadow: {
      panel: '0 2px 12px rgba(0,212,255,0.08)',
      hover: '0 4px 20px rgba(0,212,255,0.15)',
      card: '0 2px 8px rgba(0,212,255,0.06)',
      modal: '0 8px 32px rgba(0,212,255,0.2)',
      mapOverlay: '0 4px 16px rgba(0,212,255,0.12)',
    },
  },

  // ========== 青绿生态风 ==========
  ecoGreen: {
    key: 'ecoGreen',
    cssKey: 'eco-green',
    name: '青绿生态',
    nameEn: 'Eco Green',
    description: '适用于生态环境、水利水务、智慧农业、碳排放监测',
    aliases: ['tourism'], // 向后兼容旧键名

    colors: {
      bgPage: '#0A1A2A',
      bgPanel: 'rgba(6, 42, 42, 0.8)',
      bgPanelSolid: '#0C2A2A',
      bgCard: 'rgba(0, 30, 25, 0.5)',

      primary: '#00E5C3',
      primaryRgb: '0, 229, 195',
      secondary: '#00FF88',
      accent: '#00BFA5',

      success: '#00FF88',
      warning: '#FFD93D',
      danger: '#FF6B6B',
      info: '#00E5C3',

      titleColor: '#FFFFFF',
      panelTitleColor: '#00E5C3',
      textPrimary: '#E0FFF0',
      textMuted: '#5A8A7A',
      highlightColor: '#00FF88',

      borderPanel: 'rgba(0, 229, 195, 0.3)',
      borderGlow: 'rgba(0, 229, 195, 0.6)',

      chartColors: ['#00E5C3', '#00FF88', '#44FFAA', '#26C6DA', '#FFD93D', '#FF8C42', '#00BFA5', '#FF69B4'],
    },

    gradients: {
      primary: 'linear-gradient(to top, #005A4A, #00E5C3)',
      secondary: 'linear-gradient(to top, #005A30, #00FF88)',
      area: 'linear-gradient(to bottom, rgba(0,229,195,0.3), transparent)',
      panel: 'linear-gradient(180deg, rgba(6,42,42,0.9), rgba(2,30,30,0.9))',
      glowBar: 'linear-gradient(90deg, transparent, #00E5C3, transparent)',
    },

    decoration: {
      cornerStyle: 'wave',
      headerStyle: 'waveLine',
      glowEffect: true,
      particleEffect: false,
      flylineEffect: true,
    },

    animation: {
      intensity: 'medium',
      breathe: true,
      scanLine: false,
    },

    map: {
      areaColor: '#0a2a22',
      borderColor: '#00E5C3',
      borderWidth: 1,
      emphasisAreaColor: '#1a4a3a',
      emphasisBorderColor: '#FFD93D',
    },

    chart: {
      backgroundColor: 'transparent',
      textColor: '#E0FFF0',
      axisLineColor: 'rgba(0, 229, 195, 0.3)',
      splitLineColor: 'rgba(0, 229, 195, 0.1)',
      axisLabelColor: '#5A8A7A',
    },

    font: {
      title: "'Source Han Sans CN', 'Microsoft YaHei Bold', sans-serif",
      data: "'DIN Alternate', 'Roboto-Bold', 'Helvetica Bold', sans-serif",
      body: "'Microsoft YaHei', 'PingFang SC', sans-serif",
    },

    button: {
      primaryBg: 'linear-gradient(135deg, #00BFA5, #00E5C3)',
      primaryText: '#FFFFFF',
      secondaryText: '#00E5C3',
      secondaryBorder: 'rgba(0, 229, 195, 0.5)',
      dangerBg: 'linear-gradient(135deg, #CC3333, #FF6B6B)',
      hoverOverlay: 'rgba(255, 255, 255, 0.15)',
      activeOverlay: 'rgba(0, 0, 0, 0.1)',
      disabledBg: 'rgba(255, 255, 255, 0.1)',
      disabledText: 'rgba(255, 255, 255, 0.3)',
    },

    tab: {
      capsuleBg: 'rgba(0, 229, 195, 0.08)',
      activeBg: 'linear-gradient(135deg, #00BFA5, #00E5C3)',
    },

    titleBar: {
      bgTitleBar: 'rgba(0, 229, 195, 0.15)',
      gradientHeaderBg: 'linear-gradient(180deg, rgba(0,229,195,0.12), transparent)',
      gradientHeaderGlow: 'linear-gradient(90deg, transparent, #00E5C3, transparent)',
      gradientTitleText: 'linear-gradient(90deg, #00E5C3, #FFFFFF 50%, #00E5C3)',
      gradientPanelTitleText: 'linear-gradient(90deg, #00E5C3, #FFFFFF)',
    },

    shadow: {
      panel: '0 2px 12px rgba(0,229,195,0.08)',
      hover: '0 4px 20px rgba(0,229,195,0.15)',
      card: '0 2px 8px rgba(0,229,195,0.06)',
      modal: '0 8px 32px rgba(0,229,195,0.2)',
      mapOverlay: '0 4px 16px rgba(0,229,195,0.12)',
    },
  },

  // ========== 党建红金风 ==========
  partyRed: {
    key: 'partyRed',
    cssKey: 'party-red',
    name: '党建红金',
    nameEn: 'Party Red',
    description: '适用于智慧党建、政务大厅、廉政监督、红色文旅',
    aliases: [],

    colors: {
      bgPage: '#1A0A0A',
      bgPanel: 'rgba(60, 15, 15, 0.8)',
      bgPanelSolid: '#2A1414',
      bgCard: 'rgba(80, 20, 20, 0.5)',

      primary: '#FF4D4F',
      primaryRgb: '255, 77, 79',
      secondary: '#FFD700',
      accent: '#FF8C00',

      success: '#44FFAA',
      warning: '#FFD700',
      danger: '#FF4D4F',
      info: '#FFB347',

      titleColor: '#FFFFFF',
      panelTitleColor: '#FFD700',
      textPrimary: '#FFE0E0',
      textMuted: '#8A6A6A',
      highlightColor: '#FF4D4F',

      borderPanel: 'rgba(255, 77, 79, 0.4)',
      borderGlow: 'rgba(255, 215, 0, 0.6)',

      chartColors: ['#FF4D4F', '#FFD700', '#FF8C00', '#FFFFFF', '#FF69B4', '#44FFAA', '#FFB347', '#FF6B6B'],
    },

    gradients: {
      primary: 'linear-gradient(to top, #8A0000, #FF4D4F)',
      secondary: 'linear-gradient(to top, #8A6A00, #FFD700)',
      area: 'linear-gradient(to bottom, rgba(255,77,79,0.3), transparent)',
      panel: 'linear-gradient(180deg, rgba(60,15,15,0.9), rgba(40,8,8,0.9))',
      glowBar: 'linear-gradient(90deg, transparent, #FFD700, transparent)',
    },

    decoration: {
      cornerStyle: 'gold',
      headerStyle: 'partyIcon',
      glowEffect: true,
      particleEffect: false,
      flylineEffect: false,
    },

    animation: {
      intensity: 'medium',
      breathe: true,
      scanLine: false,
    },

    map: {
      areaColor: '#3d0a0a',
      borderColor: '#FFD700',
      borderWidth: 1,
      emphasisAreaColor: '#5a1515',
      emphasisBorderColor: '#FFD700',
    },

    chart: {
      backgroundColor: 'transparent',
      textColor: '#FFE0E0',
      axisLineColor: 'rgba(255, 215, 0, 0.2)',
      splitLineColor: 'rgba(255, 215, 0, 0.1)',
      axisLabelColor: '#8A6A6A',
    },

    font: {
      title: "'SimSun', 'STSong', 'Source Han Sans CN', 'Microsoft YaHei Bold', sans-serif",
      data: "'DIN Alternate', 'Roboto-Bold', 'Helvetica Bold', sans-serif",
      body: "'Microsoft YaHei', 'SimSun', 'PingFang SC', sans-serif",
    },

    button: {
      primaryBg: 'linear-gradient(135deg, #FF4D4F, #FF8C00)',
      primaryText: '#FFFFFF',
      secondaryText: '#FFD700',
      secondaryBorder: 'rgba(255, 215, 0, 0.5)',
      dangerBg: 'linear-gradient(135deg, #CC0000, #FF4D4F)',
      hoverOverlay: 'rgba(255, 255, 255, 0.15)',
      activeOverlay: 'rgba(0, 0, 0, 0.1)',
      disabledBg: 'rgba(255, 255, 255, 0.1)',
      disabledText: 'rgba(255, 255, 255, 0.3)',
    },

    tab: {
      capsuleBg: 'rgba(255, 215, 0, 0.08)',
      activeBg: 'linear-gradient(135deg, #CC0000, #FF4D4F)',
    },

    titleBar: {
      bgTitleBar: 'rgba(255, 215, 0, 0.15)',
      gradientHeaderBg: 'linear-gradient(180deg, rgba(255,215,0,0.15), transparent)',
      gradientHeaderGlow: 'linear-gradient(90deg, transparent, #FFD700, transparent)',
      gradientTitleText: 'linear-gradient(90deg, #FFD700, #FFFFFF 50%, #FFD700)',
      gradientPanelTitleText: 'linear-gradient(90deg, #FFD700, #FFFFFF)',
    },

    shadow: {
      panel: '0 2px 12px rgba(255,215,0,0.08)',
      hover: '0 4px 20px rgba(255,215,0,0.15)',
      card: '0 2px 8px rgba(255,215,0,0.06)',
      modal: '0 8px 32px rgba(255,215,0,0.2)',
      mapOverlay: '0 4px 16px rgba(255,215,0,0.12)',
    },
  },

  // ========== 暖橙数据风 ==========
  warmOrange: {
    key: 'warmOrange',
    cssKey: 'warm-orange',
    name: '暖橙数据',
    nameEn: 'Warm Orange',
    description: '适用于经济运行分析、产业发展、GDP分析、招商引资',
    aliases: [],

    colors: {
      bgPage: '#1A1210',
      bgPanel: 'rgba(50, 35, 15, 0.8)',
      bgPanelSolid: '#1E1A14',
      bgCard: 'rgba(40, 30, 15, 0.5)',

      primary: '#FF8C42',
      primaryRgb: '255, 140, 66',
      secondary: '#FFB347',
      accent: '#FFD93D',

      success: '#44FFAA',
      warning: '#FFD93D',
      danger: '#FF6B6B',
      info: '#FFB347',

      titleColor: '#FFFFFF',
      panelTitleColor: '#FF8C42',
      textPrimary: '#FFF0E0',
      textMuted: '#8A7A6A',
      highlightColor: '#FFD93D',

      borderPanel: 'rgba(255, 140, 66, 0.3)',
      borderGlow: 'rgba(255, 140, 66, 0.6)',

      chartColors: ['#FF8C42', '#FFB347', '#FFD93D', '#FF6B6B', '#44FFAA', '#A855F7', '#00D4FF', '#FF69B4'],
    },

    gradients: {
      primary: 'linear-gradient(to top, #8A4500, #FF8C42)',
      secondary: 'linear-gradient(to top, #8A6A00, #FFB347)',
      area: 'linear-gradient(to bottom, rgba(255,140,66,0.3), transparent)',
      panel: 'linear-gradient(180deg, rgba(50,35,15,0.9), rgba(30,20,8,0.9))',
      glowBar: 'linear-gradient(90deg, transparent, #FF8C42, transparent)',
    },

    decoration: {
      cornerStyle: 'simple',
      headerStyle: 'gradient',
      glowEffect: true,
      particleEffect: false,
      flylineEffect: false,
    },

    animation: {
      intensity: 'light',
      breathe: true,
      scanLine: false,
    },

    map: {
      areaColor: '#1a1a0a',
      borderColor: '#FF8C42',
      borderWidth: 1,
      emphasisAreaColor: '#2a2a1a',
      emphasisBorderColor: '#FFD93D',
    },

    chart: {
      backgroundColor: 'transparent',
      textColor: '#FFF0E0',
      axisLineColor: 'rgba(255, 140, 66, 0.3)',
      splitLineColor: 'rgba(255, 140, 66, 0.1)',
      axisLabelColor: '#8A7A6A',
    },

    font: {
      title: "'Source Han Sans CN', 'Microsoft YaHei Bold', sans-serif",
      data: "'DIN Alternate', 'Roboto-Bold', 'Helvetica Bold', sans-serif",
      body: "'Microsoft YaHei', 'PingFang SC', sans-serif",
    },

    button: {
      primaryBg: 'linear-gradient(135deg, #FF8C42, #FFB347)',
      primaryText: '#FFFFFF',
      secondaryText: '#FF8C42',
      secondaryBorder: 'rgba(255, 140, 66, 0.5)',
      dangerBg: 'linear-gradient(135deg, #CC3333, #FF6B6B)',
      hoverOverlay: 'rgba(255, 255, 255, 0.15)',
      activeOverlay: 'rgba(0, 0, 0, 0.1)',
      disabledBg: 'rgba(255, 255, 255, 0.1)',
      disabledText: 'rgba(255, 255, 255, 0.3)',
    },

    tab: {
      capsuleBg: 'rgba(255, 140, 66, 0.08)',
      activeBg: 'linear-gradient(135deg, #FF8C42, #FFB347)',
    },

    titleBar: {
      bgTitleBar: 'rgba(255, 140, 66, 0.15)',
      gradientHeaderBg: 'linear-gradient(180deg, rgba(255,140,66,0.10), transparent)',
      gradientHeaderGlow: 'linear-gradient(90deg, transparent, #FF8C42, transparent)',
      gradientTitleText: 'linear-gradient(90deg, #FF8C42, #FFFFFF 50%, #FF8C42)',
      gradientPanelTitleText: 'linear-gradient(90deg, #FF8C42, #FFFFFF)',
    },

    shadow: {
      panel: '0 2px 12px rgba(255,140,66,0.08)',
      hover: '0 4px 20px rgba(255,140,66,0.15)',
      card: '0 2px 8px rgba(255,140,66,0.06)',
      modal: '0 8px 32px rgba(255,140,66,0.2)',
      mapOverlay: '0 4px 16px rgba(255,140,66,0.12)',
    },
  },

  // ========== 紫蓝深邃风 ==========
  deepPurple: {
    key: 'deepPurple',
    cssKey: 'deep-purple',
    name: '紫蓝深邃',
    nameEn: 'Deep Purple',
    description: '适用于数字孪生、3D可视化、城市大脑、应急管理',
    aliases: [],

    colors: {
      bgPage: '#0E0A20',
      bgPanel: 'rgba(20, 16, 60, 0.8)',
      bgPanelSolid: '#14103A',
      bgCard: 'rgba(15, 10, 45, 0.5)',

      primary: '#A855F7',
      primaryRgb: '168, 85, 247',
      secondary: '#6366F1',
      accent: '#C084FC',

      success: '#44FFAA',
      warning: '#FFD93D',
      danger: '#FF6B6B',
      info: '#6366F1',

      titleColor: '#FFFFFF',
      panelTitleColor: '#A855F7',
      textPrimary: '#E8E0FF',
      textMuted: '#7A6A8A',
      highlightColor: '#C084FC',

      borderPanel: 'rgba(168, 85, 247, 0.3)',
      borderGlow: 'rgba(168, 85, 247, 0.6)',

      chartColors: ['#A855F7', '#6366F1', '#C084FC', '#00D4FF', '#FF6B6B', '#FFD93D', '#44FFAA', '#FF69B4'],
    },

    gradients: {
      primary: 'linear-gradient(to top, #3B0086, #A855F7)',
      secondary: 'linear-gradient(to top, #1A0086, #6366F1)',
      area: 'linear-gradient(to bottom, rgba(168,85,247,0.3), transparent)',
      panel: 'linear-gradient(180deg, rgba(20,16,60,0.9), rgba(10,8,40,0.9))',
      glowBar: 'linear-gradient(90deg, transparent, #A855F7, transparent)',
    },

    decoration: {
      cornerStyle: 'tech',
      headerStyle: 'dotMatrix',
      glowEffect: true,
      particleEffect: true,
      flylineEffect: true,
    },

    animation: {
      intensity: 'strong',
      breathe: true,
      scanLine: true,
    },

    map: {
      areaColor: '#0a0a2a',
      borderColor: '#A855F7',
      borderWidth: 1,
      emphasisAreaColor: '#1a1a4a',
      emphasisBorderColor: '#C084FC',
    },

    chart: {
      backgroundColor: 'transparent',
      textColor: '#E8E0FF',
      axisLineColor: 'rgba(168, 85, 247, 0.3)',
      splitLineColor: 'rgba(168, 85, 247, 0.1)',
      axisLabelColor: '#7A6A8A',
    },

    font: {
      title: "'Source Han Sans CN', 'Microsoft YaHei Bold', sans-serif",
      data: "'DIN Alternate', 'Roboto-Bold', 'Helvetica Bold', sans-serif",
      body: "'Microsoft YaHei', 'PingFang SC', sans-serif",
    },

    button: {
      primaryBg: 'linear-gradient(135deg, #6366F1, #A855F7)',
      primaryText: '#FFFFFF',
      secondaryText: '#A855F7',
      secondaryBorder: 'rgba(168, 85, 247, 0.5)',
      dangerBg: 'linear-gradient(135deg, #CC3333, #FF6B6B)',
      hoverOverlay: 'rgba(255, 255, 255, 0.15)',
      activeOverlay: 'rgba(0, 0, 0, 0.1)',
      disabledBg: 'rgba(255, 255, 255, 0.1)',
      disabledText: 'rgba(255, 255, 255, 0.3)',
    },

    tab: {
      capsuleBg: 'rgba(168, 85, 247, 0.08)',
      activeBg: 'linear-gradient(135deg, #6366F1, #A855F7)',
    },

    titleBar: {
      bgTitleBar: 'rgba(168, 85, 247, 0.15)',
      gradientHeaderBg: 'linear-gradient(180deg, rgba(168,85,247,0.15), transparent)',
      gradientHeaderGlow: 'linear-gradient(90deg, transparent, #A855F7, transparent)',
      gradientTitleText: 'linear-gradient(90deg, #A855F7, #FFFFFF 50%, #A855F7)',
      gradientPanelTitleText: 'linear-gradient(90deg, #A855F7, #C084FC)',
    },

    shadow: {
      panel: '0 2px 12px rgba(168,85,247,0.08)',
      hover: '0 4px 20px rgba(168,85,247,0.15)',
      card: '0 2px 8px rgba(168,85,247,0.06)',
      modal: '0 8px 32px rgba(168,85,247,0.2)',
      mapOverlay: '0 4px 16px rgba(168,85,247,0.12)',
    },
  },

  // ========== 浅色商务风 ==========
  lightBusiness: {
    key: 'lightBusiness',
    cssKey: 'light-business',
    name: '浅色商务',
    nameEn: 'Light Business',
    description: '适用于企业管理后台、运营报表、会议室展示、SaaS仪表盘',
    aliases: ['lightBright'], // 向后兼容旧键名

    colors: {
      bgPage: '#F0F2F5',
      bgPanel: 'rgba(255, 255, 255, 0.95)',
      bgPanelSolid: '#FFFFFF',
      bgCard: '#FAFAFA',

      primary: '#1890FF',
      primaryRgb: '24, 144, 255',
      secondary: '#52C41A',
      accent: '#FAAD14',

      success: '#52C41A',
      warning: '#FAAD14',
      danger: '#FF4D4F',
      info: '#1890FF',

      titleColor: '#262626',
      panelTitleColor: '#1890FF',
      textPrimary: '#595959',
      textMuted: '#8C8C8C',
      highlightColor: '#1890FF',

      borderPanel: '#E8E8E8',
      borderGlow: 'transparent',

      chartColors: ['#1890FF', '#52C41A', '#FAAD14', '#F5222D', '#722ED1', '#13C2C2', '#EB2F96', '#2F54EB'],
    },

    gradients: {
      primary: 'linear-gradient(to top, #096DD9, #1890FF)',
      secondary: 'linear-gradient(to top, #237804, #52C41A)',
      area: 'linear-gradient(to bottom, rgba(24,144,255,0.15), transparent)',
      panel: 'linear-gradient(180deg, #FFFFFF, #FAFAFA)',
      glowBar: 'none',
    },

    decoration: {
      cornerStyle: 'none',
      headerStyle: 'gradient',
      glowEffect: false,
      particleEffect: false,
      flylineEffect: false,
    },

    animation: {
      intensity: 'minimal',
      breathe: false,
      scanLine: false,
    },

    map: {
      areaColor: '#F0F2F5',
      borderColor: '#1890FF',
      borderWidth: 1,
      emphasisAreaColor: '#E6F7FF',
      emphasisBorderColor: '#1890FF',
    },

    chart: {
      backgroundColor: '#FFFFFF',
      textColor: '#595959',
      axisLineColor: '#E8E8E8',
      splitLineColor: '#F0F0F0',
      axisLabelColor: '#8C8C8C',
    },

    font: {
      title: "'Source Han Sans CN', 'Microsoft YaHei Bold', sans-serif",
      data: "'DIN Alternate', 'Roboto-Bold', 'Helvetica Bold', sans-serif",
      body: "'Microsoft YaHei', 'PingFang SC', sans-serif",
    },

    button: {
      primaryBg: '#1890FF',
      primaryText: '#FFFFFF',
      secondaryText: '#1890FF',
      secondaryBorder: '#1890FF',
      dangerBg: '#FF4D4F',
      hoverOverlay: 'rgba(255, 255, 255, 0.15)',
      activeOverlay: 'rgba(0, 0, 0, 0.1)',
      disabledBg: 'rgba(0, 0, 0, 0.04)',
      disabledText: 'rgba(0, 0, 0, 0.25)',
    },

    tab: {
      capsuleBg: '#F0F0F0',
      activeBg: '#1890FF',
    },

    titleBar: {
      bgTitleBar: '#F0F5FF',
      gradientHeaderBg: 'linear-gradient(180deg, #FFFFFF, #F0F2F5)',
      gradientHeaderGlow: 'none',
      gradientTitleText: 'none',
      gradientPanelTitleText: 'none',
    },

    shadow: {
      panel: '0 2px 8px rgba(0,0,0,0.06)',
      hover: '0 4px 16px rgba(0,0,0,0.1)',
      card: '0 2px 6px rgba(0,0,0,0.04)',
      modal: '0 8px 24px rgba(0,0,0,0.15)',
      mapOverlay: '0 4px 12px rgba(0,0,0,0.08)',
    },
  },
}

// ========== 向后兼容键名映射 ==========
// 旧键名 → 新键名
export const legacyThemeMap = {
  darkTech: 'techBlue',
  tourism: 'ecoGreen',
  lightBright: 'lightBusiness',
  // partyRed 保持不变
}

// 解析主题键名（支持旧键名自动映射）
export function resolveThemeKey(key) {
  return legacyThemeMap[key] || key
}

// 默认主题
export const defaultTheme = 'techBlue'

// 获取主题配置
export function getTheme(themeName) {
  const resolvedKey = resolveThemeKey(themeName)
  return themes[resolvedKey] || themes[defaultTheme]
}

// 获取所有主题名称
export function getThemeNames() {
  return Object.keys(themes).map(key => ({
    key,
    cssKey: themes[key].cssKey,
    name: themes[key].name,
    nameEn: themes[key].nameEn,
    description: themes[key].description,
    previewColors: {
      bg: themes[key].colors.bgPage,
      primary: themes[key].colors.primary,
    },
  }))
}

// 获取主题图表色板
export function getChartColors(themeName) {
  const theme = getTheme(themeName)
  return theme.chartColors
}

// 获取主题 ECharts 配置
export function getChartTheme(themeName) {
  const theme = getTheme(themeName)
  return {
    backgroundColor: theme.chart.backgroundColor,
    textStyle: { color: theme.chart.textColor, fontSize: 12 },
    title: { textStyle: { color: theme.colors.panelTitleColor, fontSize: 14 } },
    legend: { textStyle: { color: theme.chart.textColor } },
    categoryAxis: {
      axisLine: { lineStyle: { color: theme.chart.axisLineColor } },
      axisLabel: { color: theme.chart.axisLabelColor },
      splitLine: { lineStyle: { color: theme.chart.splitLineColor } },
    },
    valueAxis: {
      axisLine: { show: false },
      axisLabel: { color: theme.chart.axisLabelColor },
      splitLine: { lineStyle: { color: theme.chart.splitLineColor } },
    },
    color: theme.chartColors,
  }
}
```

---

## 二、CSS 变量生成 (themes/css-variables.js)

```javascript
/**
 * 根据主题配置生成 CSS 变量
 * 包含颜色、渐变、面板、地图、图表、装饰、动画、字体全量变量
 */

export function generateCssVariables(theme) {
  const { colors, gradients, decoration, animation, map, chart, font, button, tab, titleBar, shadow } = theme

  return `
:root[data-theme="${theme.cssKey}"] {
  /* 背景色 */
  --bg-page: ${colors.bgPage};
  --bg-panel: ${colors.bgPanel};
  --bg-panel-solid: ${colors.bgPanelSolid};
  --bg-card: ${colors.bgCard};

  /* 强调色 */
  --color-primary: ${colors.primary};
  --color-primary-rgb: ${colors.primaryRgb};
  --color-secondary: ${colors.secondary};
  --color-accent: ${colors.accent};

  /* 状态色 */
  --color-success: ${colors.success};
  --color-warning: ${colors.warning};
  --color-danger: ${colors.danger};
  --color-info: ${colors.info};

  /* 文字色 */
  --color-title: ${colors.titleColor};
  --color-panel-title: ${colors.panelTitleColor};
  --color-text: ${colors.textPrimary};
  --color-text-muted: ${colors.textMuted};
  --color-highlight: ${colors.highlightColor};

  /* 边框色 */
  --border-panel: ${colors.borderPanel};
  --border-glow: ${colors.borderGlow};

  /* 渐变色 */
  --gradient-primary: ${gradients.primary};
  --gradient-secondary: ${gradients.secondary};
  --gradient-area: ${gradients.area};
  --gradient-panel: ${gradients.panel};
  --gradient-glow-bar: ${gradients.glowBar};

  /* 标题栏 */
  --bg-title-bar: ${titleBar.bgTitleBar};
  --gradient-header-bg: ${titleBar.gradientHeaderBg};
  --gradient-header-glow: ${titleBar.gradientHeaderGlow};
  --gradient-title-text: ${titleBar.gradientTitleText};
  --gradient-panel-title-text: ${titleBar.gradientPanelTitleText};

  /* 按钮 */
  --btn-primary-bg: ${button.primaryBg};
  --btn-primary-text: ${button.primaryText};
  --btn-secondary-text: ${button.secondaryText};
  --btn-secondary-border: ${button.secondaryBorder};
  --btn-danger-bg: ${button.dangerBg};
  --btn-hover-overlay: ${button.hoverOverlay};
  --btn-active-overlay: ${button.activeOverlay};
  --btn-disabled-bg: ${button.disabledBg};
  --btn-disabled-text: ${button.disabledText};

  /* Tab 切换 */
  --tab-capsule-bg: ${tab.capsuleBg};
  --tab-active-bg: ${tab.activeBg};

  /* 装饰配置 */
  --corner-style: ${decoration.cornerStyle};
  --header-style: ${decoration.headerStyle};
  --glow-effect: ${decoration.glowEffect};
  --particle-effect: ${decoration.particleEffect};
  --flyline-effect: ${decoration.flylineEffect};

  /* 动画配置 */
  --animation-intensity: ${animation.intensity};
  --breathe-enabled: ${animation.breathe};
  --scanline-enabled: ${animation.scanLine};

  /* 地图 */
  --map-area-color: ${map.areaColor};
  --map-border-color: ${map.borderColor};

  /* 图表 */
  --chart-bg: ${chart.backgroundColor};
  --chart-text: ${chart.textColor};
  --chart-axis-line: ${chart.axisLineColor};
  --chart-split-line: ${chart.splitLineColor};
  --shadow-panel: ${shadow.panel};
  --shadow-hover: ${shadow.hover};
  --shadow-card: ${shadow.card};
  --shadow-modal: ${shadow.modal};
  --shadow-map-overlay: ${shadow.mapOverlay};

  /* Badge 状态色 */
  --badge-success: #52C41A;
  --badge-danger: #FF4D4F;
  --badge-warning: #FAAD14;
  --badge-info: #1890FF;
  --badge-completed: #52C41A;
  --badge-closed: rgba(255, 255, 255, 0.35);

  /* Z-index 层级 */
  --z-bg: 0;
  --z-content: 5;
  --z-map: 10;
  --z-map-overlay: 20;
  --z-map-float: 30;
  --z-tooltip: 45;
  --z-header: 55;
  --z-mask: 65;
  --z-modal: 70;
  --z-notify: 90;

  /* 滚动条 */
  --scrollbar-width: 6px;
  --scrollbar-track: transparent;
  --scrollbar-thumb: rgba(${colors.primaryRgb}, 0.25);
  --scrollbar-thumb-hover: rgba(${colors.primaryRgb}, 0.40);

  /* 间距刻度 */
  --spacing-unit: 4px;

  /* 过渡时长 */
  --duration-fast: 150ms;
  --duration-normal: 200ms;
  --duration-slow: 300ms;
  --duration-slower: 500ms;
  --duration-slowest: 800ms;
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* 字体 */
  --font-title: ${font.title};
  --font-data: ${font.data};
  --font-body: ${font.body};
}
  `.trim()
}

/**
 * 生成所有主题的 CSS 变量样式表
 */
export function generateAllThemeStyles() {
  return Object.values(themes)
    .map(theme => generateCssVariables(theme))
    .join('\n\n')
}
```

---

## 三、主题 SCSS 变量 (themes/theme-variables.scss)

```scss
// BI 大屏主题 SCSS 变量
// 所有值通过 CSS 变量引用，支持主题切换

// ========== 颜色变量 ==========
$bg-page: var(--bg-page);
$bg-panel: var(--bg-panel);
$bg-panel-solid: var(--bg-panel-solid);
$bg-card: var(--bg-card);

$color-primary: var(--color-primary);
$color-primary-rgb: var(--color-primary-rgb);
$color-secondary: var(--color-secondary);
$color-accent: var(--color-accent);

$color-success: var(--color-success);
$color-warning: var(--color-warning);
$color-danger: var(--color-danger);
$color-info: var(--color-info);

$color-title: var(--color-title);
$color-panel-title: var(--color-panel-title);
$color-text: var(--color-text);
$color-text-muted: var(--color-text-muted);
$color-highlight: var(--color-highlight);

$border-panel: var(--border-panel);
$border-glow: var(--border-glow);

// ========== 渐变变量 ==========
$gradient-primary: var(--gradient-primary);
$gradient-secondary: var(--gradient-secondary);
$gradient-area: var(--gradient-area);
$gradient-panel: var(--gradient-panel);
$gradient-glow-bar: var(--gradient-glow-bar);

// ========== 标题栏变量 ==========
$bg-title-bar: var(--bg-title-bar);
$gradient-header-bg: var(--gradient-header-bg);
$gradient-header-glow: var(--gradient-header-glow);
$gradient-title-text: var(--gradient-title-text);
$gradient-panel-title-text: var(--gradient-panel-title-text);

// ========== 按钮变量 ==========
$btn-primary-bg: var(--btn-primary-bg);
$btn-primary-text: var(--btn-primary-text);
$btn-secondary-text: var(--btn-secondary-text);
$btn-secondary-border: var(--btn-secondary-border);
$btn-danger-bg: var(--btn-danger-bg);

// ========== Tab 变量 ==========
$tab-capsule-bg: var(--tab-capsule-bg);
$tab-active-bg: var(--tab-active-bg);

// ========== 字体变量 ==========
$font-title: var(--font-title);
$font-data: var(--font-data);
$font-body: var(--font-body);
```

---

## 四、通用组件样式 (themes/common-components.scss)

```scss
// BI 大屏通用组件样式
// 所有颜色通过 CSS 变量引用，自动跟随主题

// ========== 面板样式 ==========
.panel-frame {
  background: $bg-panel;
  border: 1px solid $border-panel;
  border-radius: 4px;
  padding: 14px;
  position: relative;
}

.panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  background: rgba(0, 0, 0, 0.15);
  position: relative;

  // 顶部光条
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: $gradient-glow-bar;
  }
}

.panel-title {
  display: flex;
  align-items: center;
  font-size: 14px;
  font-weight: 500;
  color: $color-panel-title;
  font-family: $font-title;

  .title-bar {
    width: 3px;
    height: 16px;
    background: $color-primary;
    margin-right: 8px;
    border-radius: 2px;
  }
}

// ========== 标题栏样式 ==========
.bi-header {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: $gradient-panel;
  border-bottom: 1px solid $border-panel;
  position: relative;

  // 两侧光带装饰
  &::before, &::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 200px;
    height: 2px;
    background: $gradient-glow-bar;
  }

  &::before { left: 20%; }
  &::after { right: 20%; }
}

.header-title {
  font-size: 28px;
  font-weight: bold;
  color: $color-title;
  letter-spacing: 4px;
  font-family: $font-title;
  text-shadow: 0 0 20px $border-glow;
}

// ========== 数据卡片样式 ==========
.data-card {
  display: flex;
  align-items: flex-start;
  padding: 16px;
  background: $bg-card;
  border: 1px solid $border-panel;
  border-radius: 8px;
  transition: all 0.3s;

  &:hover {
    border-color: $color-primary;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px $border-glow;
  }
}

.data-value {
  font-size: 28px;
  font-weight: bold;
  color: $color-title;
  font-family: $font-data;
}

.data-label {
  font-size: 14px;
  color: $color-text-muted;
  font-family: $font-body;
}

// ========== 角标装饰 ==========
.corner-decoration {
  position: absolute;
  width: 12px;
  height: 12px;

  &.corner-tl {
    top: -1px; left: -1px;
    border-top: 2px solid $color-primary;
    border-left: 2px solid $color-primary;
  }
  &.corner-tr {
    top: -1px; right: -1px;
    border-top: 2px solid $color-primary;
    border-right: 2px solid $color-primary;
  }
  &.corner-bl {
    bottom: -1px; left: -1px;
    border-bottom: 2px solid $color-primary;
    border-left: 2px solid $color-primary;
  }
  &.corner-br {
    bottom: -1px; right: -1px;
    border-bottom: 2px solid $color-primary;
    border-right: 2px solid $color-primary;
  }
}

// ========== 顶部光条 ==========
.glow-bar {
  height: 2px;
  background: $gradient-glow-bar;
}

// ========== 呼吸动画 ==========
@keyframes breathe {
  0%, 100% {
    box-shadow: 0 0 8px $border-glow;
    border-color: $border-panel;
  }
  50% {
    box-shadow: 0 0 20px $border-glow;
    border-color: $color-primary;
  }
}

.panel-breathe {
  animation: breathe 3s ease-in-out infinite;
}

// ========== 图表容器 ==========
.chart-container {
  background: $bg-card;
}

.chart-axis-line {
  stroke: var(--chart-axis-line);
}

.chart-split-line {
  stroke: var(--chart-split-line);
}

.chart-text {
  fill: var(--chart-text);
}

// ========== 面板标题变体 ==========

// 变体 A — 竖线 + 文字（默认）
.panel-title-variant-a {
  border-left: 3px solid $color-primary;
  padding-left: 8px;
  color: $color-panel-title;
  font-size: 14px;
  font-weight: 500;
}

// 变体 B — 渐变背景条 + 文字
.panel-title-variant-b {
  padding: 8px 12px;
  background: linear-gradient(90deg, $bg-title-bar, transparent);
  color: $color-panel-title;
  font-size: 14px;
  font-weight: 500;
}

// 变体 C — 下划线装饰 + 文字
.panel-title-variant-c {
  padding: 8px 0;
  border-bottom: 1px solid $border-panel;
  color: $color-panel-title;
  font-size: 14px;
  font-weight: 500;
  &::after {
    content: '';
    display: block;
    width: 60px;
    height: 2px;
    margin-top: 4px;
    background: linear-gradient(90deg, $color-primary, transparent);
  }
}

// 变体 D — 图标 + 文字
.panel-title-variant-d {
  display: flex;
  align-items: center;
  gap: 6px;
  color: $color-panel-title;
  font-size: 14px;
  .icon {
    width: 16px;
    height: 16px;
    color: $color-primary;
  }
}

// ========== 按钮样式 ==========
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: inherit;
  border: none;
  outline: none;
}

.btn-primary {
  background: $btn-primary-bg;
  color: $btn-primary-text;
  &:hover { box-shadow: 0 0 12px $border-glow; }
}

.btn-secondary {
  background: transparent;
  color: $btn-secondary-text;
  border: 1px solid $btn-secondary-border;
  &:hover {
    background: rgba($color-primary-rgb, 0.1);
    border-color: $color-primary;
  }
}

.btn-danger {
  background: $btn-danger-bg;
  color: #FFFFFF;
}

// 尺寸
.btn-lg { height: 36px; padding: 0 20px; font-size: 14px; }
.btn-default { height: 32px; padding: 0 16px; font-size: 13px; }
.btn-sm { height: 26px; padding: 0 12px; font-size: 12px; border-radius: 3px; }
.btn-xs { height: 22px; padding: 0 8px; font-size: 11px; border-radius: 2px; }

// ========== Tab 切换样式 ==========

// 下划线式
.tab-underline {
  display: flex;
  gap: 4px;
  .tab-item {
    padding: 6px 12px;
    color: $color-text-muted;
    font-size: 12px;
    border-bottom: 2px solid transparent;
    cursor: pointer;
    transition: all 0.2s;
    &.active {
      color: $color-primary;
      border-bottom-color: $color-primary;
    }
  }
}

// 胶囊式
.tab-capsule {
  display: flex;
  background: $tab-capsule-bg;
  border-radius: 4px;
  padding: 2px;
  .tab-item {
    padding: 4px 12px;
    border-radius: 3px;
    color: $color-text-muted;
    font-size: 12px;
    cursor: pointer;
    transition: all 0.2s;
    &.active {
      background: $tab-active-bg;
      color: #FFFFFF;
    }
  }
}

// ========== 页面标题栏 ==========
.page-header {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  background: $gradient-header-bg;

  // 底部光条
  &::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 10%;
    right: 10%;
    height: 2px;
    background: $gradient-header-glow;
  }
}

.page-title {
  font-size: 28px;
  font-weight: bold;
  font-family: $font-title;
  background: $gradient-title-text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

// 两翼装饰
.page-header .wing-left,
.page-header .wing-right {
  width: 200px;
  height: 2px;
}

.page-header .wing-left {
  background: linear-gradient(90deg, transparent, $color-primary);
}

.page-header .wing-right {
  background: linear-gradient(90deg, $color-primary, transparent);
}

.page-header .diamond {
  width: 8px;
  height: 8px;
  background: $color-primary;
  transform: rotate(45deg);
  margin: 0 12px;
}
```

---

## 五、ThemeProvider.vue（主题切换组件）

```vue
<template>
  <div :class="['theme-container', `theme-${resolvedTheme}`]">
    <slot></slot>
  </div>
</template>

<script>
import { themes, defaultTheme, resolveThemeKey, legacyThemeMap } from './index'

export default {
  name: 'ThemeProvider',
  props: {
    theme: {
      type: String,
      default: defaultTheme,
    },
  },
  data() {
    return {
      resolvedTheme: resolveThemeKey(this.theme),
    }
  },
  watch: {
    theme(val) {
      this.resolvedTheme = resolveThemeKey(val)
      this.applyTheme(this.resolvedTheme)
    },
  },
  mounted() {
    this.applyTheme(this.resolvedTheme)
  },
  methods: {
    applyTheme(themeName) {
      const resolvedKey = resolveThemeKey(themeName)
      const theme = themes[resolvedKey] || themes[defaultTheme]
      const root = document.documentElement

      // 设置 CSS 变量（颜色）
      Object.entries(theme.colors).forEach(([key, value]) => {
        // camelCase → kebab-case
        const cssVar = `--${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`
        root.style.setProperty(cssVar, value)
      })

      // 设置渐变 CSS 变量
      Object.entries(theme.gradients).forEach(([key, value]) => {
        const cssVar = `--gradient-${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`
        root.style.setProperty(cssVar, value)
      })

      // 设置装饰 CSS 变量
      Object.entries(theme.decoration).forEach(([key, value]) => {
        const cssVar = `--${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`
        root.style.setProperty(cssVar, String(value))
      })

      // 设置动画 CSS 变量
      Object.entries(theme.animation).forEach(([key, value]) => {
        const cssVar = `--${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`
        root.style.setProperty(cssVar, String(value))
      })

      // 设置字体 CSS 变量
      Object.entries(theme.font).forEach(([key, value]) => {
        const cssVar = `--font-${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`
        root.style.setProperty(cssVar, value)
      })

      // 设置按钮 CSS 变量
      if (theme.button) {
        Object.entries(theme.button).forEach(([key, value]) => {
          const cssVar = `--btn-${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`
          root.style.setProperty(cssVar, value)
        })
      }

      // 设置 Tab CSS 变量
      if (theme.tab) {
        Object.entries(theme.tab).forEach(([key, value]) => {
          const cssVar = `--tab-${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`
          root.style.setProperty(cssVar, value)
        })
      }

      // 设置标题栏 CSS 变量
      if (theme.titleBar) {
        Object.entries(theme.titleBar).forEach(([key, value]) => {
          const cssVar = `--${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`
          root.style.setProperty(cssVar, value)
        })
      }

      // 设置 data-theme 属性（用于 CSS 选择器，使用 cssKey）
      root.setAttribute('data-theme', theme.cssKey)

      // 同时设置旧的 data-theme 值（向后兼容）
      if (theme.aliases && theme.aliases.length > 0) {
        root.setAttribute('data-theme-legacy', theme.aliases[0])
      } else {
        root.removeAttribute('data-theme-legacy')
      }
    },
  },
}
</script>

<style lang="scss">
.theme-container {
  width: 100%;
  height: 100%;
}
</style>
```

---

## 六、ThemeSelector.vue（主题选择器）

```vue
<template>
  <div class="theme-selector">
    <div class="theme-label">主题切换：</div>
    <div class="theme-options">
      <div
        v-for="item in themeList"
        :key="item.key"
        :class="['theme-option', { active: currentTheme === item.key }]"
        @click="selectTheme(item.key)"
      >
        <div :class="['theme-preview', `preview-${item.key}`]"></div>
        <span class="theme-name">{{ item.name }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import { getThemeNames, defaultTheme } from './index'

export default {
  name: 'ThemeSelector',
  data() {
    return {
      currentTheme: defaultTheme,
      themeList: getThemeNames(),
    }
  },
  methods: {
    selectTheme(themeKey) {
      this.currentTheme = themeKey
      this.$emit('change', themeKey)
    },
  },
}
</script>

<style lang="scss" scoped>
.theme-selector {
  display: flex;
  align-items: center;
  gap: 12px;
}

.theme-label {
  font-size: 14px;
  color: var(--color-text-muted);
}

.theme-options {
  display: flex;
  gap: 8px;
}

.theme-option {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border: 1px solid var(--border-panel);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;

  &:hover {
    border-color: var(--color-primary);
  }

  &.active {
    border-color: var(--color-primary);
    background: var(--color-primary);
    color: #fff;
  }
}

.theme-preview {
  width: 16px;
  height: 16px;
  border-radius: 50%;

  &.preview-techBlue {
    background: linear-gradient(135deg, #0A0E27, #00D4FF);
  }

  &.preview-ecoGreen {
    background: linear-gradient(135deg, #0A1A2A, #00E5C3);
  }

  &.preview-partyRed {
    background: linear-gradient(135deg, #1A0A0A, #FFD700);
  }

  &.preview-warmOrange {
    background: linear-gradient(135deg, #1A1210, #FF8C42);
  }

  &.preview-deepPurple {
    background: linear-gradient(135deg, #0E0A20, #A855F7);
  }

  &.preview-lightBusiness {
    background: linear-gradient(135deg, #F0F2F5, #1890FF);
    border: 1px solid #E8E8E8;
  }
}

.theme-name {
  font-size: 12px;
}
</style>
```

---

## 七、主题 CSS 变量完整定义

以下为 6 套主题的 CSS 变量完整定义，可直接复制到全局样式文件中：

```css
/* ========== 深蓝科技风（默认） ========== */
:root[data-theme="tech-blue"] {
  --bg-page: #0A0E27;
  --bg-panel: rgba(6, 30, 93, 0.8);
  --bg-panel-solid: #0C1A3A;
  --bg-card: rgba(0, 20, 40, 0.5);
  --border-panel: rgba(0, 212, 255, 0.3);
  --color-primary: #00D4FF;
  --color-primary-rgb: 0, 212, 255;
  --color-secondary: #0088FF;
  --color-accent: #44FFAA;
  --color-title: #FFFFFF;
  --color-panel-title: #00D4FF;
  --color-text: #E0E8FF;
  --color-text-muted: #6B7FA3;
  --color-highlight: #FFD93D;
  --color-warning: #FF6B6B;
  --glow-color: rgba(0, 212, 255, 0.6);
  --gradient-primary: linear-gradient(to top, #003B7A, #00D4FF);
  --gradient-secondary: linear-gradient(to top, #003088, #0088FF);
  --gradient-area: linear-gradient(to bottom, rgba(0,212,255,0.3), transparent);
  --gradient-panel: linear-gradient(180deg, rgba(6,30,93,0.9), rgba(2,12,50,0.9));
  --gradient-glow-bar: linear-gradient(90deg, transparent, #00D4FF, transparent);
  --bg-title-bar: rgba(0, 212, 255, 0.15);
  --gradient-header-bg: linear-gradient(180deg, rgba(0,212,255,0.12), transparent);
  --gradient-header-glow: linear-gradient(90deg, transparent, #00D4FF, transparent);
  --gradient-title-text: linear-gradient(90deg, #00D4FF, #FFFFFF 50%, #00D4FF);
  --gradient-panel-title-text: linear-gradient(90deg, #00D4FF, #FFFFFF);
  --btn-primary-bg: linear-gradient(135deg, #0088FF, #00D4FF);
  --btn-primary-text: #FFFFFF;
  --btn-secondary-text: #00D4FF;
  --btn-secondary-border: rgba(0, 212, 255, 0.5);
  --btn-danger-bg: linear-gradient(135deg, #CC3333, #FF6B6B);
  --btn-hover-overlay: rgba(255, 255, 255, 0.15);
  --btn-active-overlay: rgba(0, 0, 0, 0.1);
  --btn-disabled-bg: rgba(255, 255, 255, 0.1);
  --btn-disabled-text: rgba(255, 255, 255, 0.3);
  --tab-capsule-bg: rgba(0, 212, 255, 0.08);
  --tab-active-bg: linear-gradient(135deg, #0088FF, #00D4FF);
  --shadow-panel: 0 2px 12px rgba(0,212,255,0.08);
  --shadow-hover: 0 4px 20px rgba(0,212,255,0.15);
  --shadow-card: 0 2px 8px rgba(0,212,255,0.06);
  --shadow-modal: 0 8px 32px rgba(0,212,255,0.2);
  --shadow-map-overlay: 0 4px 16px rgba(0,212,255,0.12);
  --badge-success: #52C41A;
  --badge-danger: #FF4D4F;
  --badge-warning: #FAAD14;
  --badge-info: #1890FF;
  --badge-completed: #52C41A;
  --badge-closed: rgba(255, 255, 255, 0.35);
  --z-bg: 0; --z-content: 5; --z-map: 10; --z-map-overlay: 20; --z-map-float: 30;
  --z-tooltip: 45; --z-header: 55; --z-mask: 65; --z-modal: 70; --z-notify: 90;
  --scrollbar-width: 6px; --scrollbar-track: transparent;
  --scrollbar-thumb: rgba(0, 212, 255, 0.25); --scrollbar-thumb-hover: rgba(0, 212, 255, 0.40);
  --spacing-unit: 4px;
  --duration-fast: 150ms; --duration-normal: 200ms; --duration-slow: 300ms;
  --duration-slower: 500ms; --duration-slowest: 800ms;
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1); --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1); --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ========== 青绿生态风 ========== */
:root[data-theme="eco-green"] {
  --bg-page: #0A1A2A;
  --bg-panel: rgba(6, 42, 42, 0.8);
  --bg-panel-solid: #0C2A2A;
  --bg-card: rgba(0, 30, 25, 0.5);
  --border-panel: rgba(0, 229, 195, 0.3);
  --color-primary: #00E5C3;
  --color-primary-rgb: 0, 229, 195;
  --color-secondary: #00FF88;
  --color-accent: #00BFA5;
  --color-title: #FFFFFF;
  --color-panel-title: #00E5C3;
  --color-text: #E0FFF0;
  --color-text-muted: #5A8A7A;
  --color-highlight: #00FF88;
  --color-warning: #FF6B6B;
  --glow-color: rgba(0, 229, 195, 0.6);
  --gradient-primary: linear-gradient(to top, #005A4A, #00E5C3);
  --gradient-secondary: linear-gradient(to top, #005A30, #00FF88);
  --gradient-area: linear-gradient(to bottom, rgba(0,229,195,0.3), transparent);
  --gradient-panel: linear-gradient(180deg, rgba(6,42,42,0.9), rgba(2,30,30,0.9));
  --gradient-glow-bar: linear-gradient(90deg, transparent, #00E5C3, transparent);
  --bg-title-bar: rgba(0, 229, 195, 0.15);
  --gradient-header-bg: linear-gradient(180deg, rgba(0,229,195,0.12), transparent);
  --gradient-header-glow: linear-gradient(90deg, transparent, #00E5C3, transparent);
  --gradient-title-text: linear-gradient(90deg, #00E5C3, #FFFFFF 50%, #00E5C3);
  --gradient-panel-title-text: linear-gradient(90deg, #00E5C3, #FFFFFF);
  --btn-primary-bg: linear-gradient(135deg, #00BFA5, #00E5C3);
  --btn-primary-text: #FFFFFF;
  --btn-secondary-text: #00E5C3;
  --btn-secondary-border: rgba(0, 229, 195, 0.5);
  --btn-danger-bg: linear-gradient(135deg, #CC3333, #FF6B6B);
  --btn-hover-overlay: rgba(255, 255, 255, 0.15);
  --btn-active-overlay: rgba(0, 0, 0, 0.1);
  --btn-disabled-bg: rgba(255, 255, 255, 0.1);
  --btn-disabled-text: rgba(255, 255, 255, 0.3);
  --tab-capsule-bg: rgba(0, 229, 195, 0.08);
  --tab-active-bg: linear-gradient(135deg, #00BFA5, #00E5C3);
  --shadow-panel: 0 2px 12px rgba(0,229,195,0.08);
  --shadow-hover: 0 4px 20px rgba(0,229,195,0.15);
  --shadow-card: 0 2px 8px rgba(0,229,195,0.06);
  --shadow-modal: 0 8px 32px rgba(0,229,195,0.2);
  --shadow-map-overlay: 0 4px 16px rgba(0,229,195,0.12);
  --badge-success: #52C41A; --badge-danger: #FF4D4F; --badge-warning: #FAAD14;
  --badge-info: #1890FF; --badge-completed: #52C41A; --badge-closed: rgba(255, 255, 255, 0.35);
  --z-bg: 0; --z-content: 5; --z-map: 10; --z-map-overlay: 20; --z-map-float: 30;
  --z-tooltip: 45; --z-header: 55; --z-mask: 65; --z-modal: 70; --z-notify: 90;
  --scrollbar-width: 6px; --scrollbar-track: transparent;
  --scrollbar-thumb: rgba(0, 229, 195, 0.25); --scrollbar-thumb-hover: rgba(0, 229, 195, 0.40);
  --spacing-unit: 4px;
  --duration-fast: 150ms; --duration-normal: 200ms; --duration-slow: 300ms;
  --duration-slower: 500ms; --duration-slowest: 800ms;
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1); --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1); --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ========== 党建红金风 ========== */
:root[data-theme="party-red"] {
  --bg-page: #1A0A0A;
  --bg-panel: rgba(60, 15, 15, 0.8);
  --bg-panel-solid: #2A1414;
  --bg-card: rgba(80, 20, 20, 0.5);
  --border-panel: rgba(255, 77, 79, 0.4);
  --color-primary: #FF4D4F;
  --color-primary-rgb: 255, 77, 79;
  --color-secondary: #FFD700;
  --color-accent: #FF8C00;
  --color-title: #FFFFFF;
  --color-panel-title: #FFD700;
  --color-text: #FFE0E0;
  --color-text-muted: #8A6A6A;
  --color-highlight: #FF4D4F;
  --color-warning: #FFD700;
  --glow-color: rgba(255, 215, 0, 0.6);
  --gradient-primary: linear-gradient(to top, #8A0000, #FF4D4F);
  --gradient-secondary: linear-gradient(to top, #8A6A00, #FFD700);
  --gradient-area: linear-gradient(to bottom, rgba(255,77,79,0.3), transparent);
  --gradient-panel: linear-gradient(180deg, rgba(60,15,15,0.9), rgba(40,8,8,0.9));
  --gradient-glow-bar: linear-gradient(90deg, transparent, #FFD700, transparent);
  --bg-title-bar: rgba(255, 215, 0, 0.15);
  --gradient-header-bg: linear-gradient(180deg, rgba(255,215,0,0.15), transparent);
  --gradient-header-glow: linear-gradient(90deg, transparent, #FFD700, transparent);
  --gradient-title-text: linear-gradient(90deg, #FFD700, #FFFFFF 50%, #FFD700);
  --gradient-panel-title-text: linear-gradient(90deg, #FFD700, #FFFFFF);
  --btn-primary-bg: linear-gradient(135deg, #FF4D4F, #FF8C00);
  --btn-primary-text: #FFFFFF;
  --btn-secondary-text: #FFD700;
  --btn-secondary-border: rgba(255, 215, 0, 0.5);
  --btn-danger-bg: linear-gradient(135deg, #CC0000, #FF4D4F);
  --btn-hover-overlay: rgba(255, 255, 255, 0.15);
  --btn-active-overlay: rgba(0, 0, 0, 0.1);
  --btn-disabled-bg: rgba(255, 255, 255, 0.1);
  --btn-disabled-text: rgba(255, 255, 255, 0.3);
  --tab-capsule-bg: rgba(255, 215, 0, 0.08);
  --tab-active-bg: linear-gradient(135deg, #CC0000, #FF4D4F);
  --shadow-panel: 0 2px 12px rgba(255,215,0,0.08);
  --shadow-hover: 0 4px 20px rgba(255,215,0,0.15);
  --shadow-card: 0 2px 8px rgba(255,215,0,0.06);
  --shadow-modal: 0 8px 32px rgba(255,215,0,0.2);
  --shadow-map-overlay: 0 4px 16px rgba(255,215,0,0.12);
  --badge-success: #52C41A; --badge-danger: #FF4D4F; --badge-warning: #FAAD14;
  --badge-info: #1890FF; --badge-completed: #52C41A; --badge-closed: rgba(255, 255, 255, 0.35);
  --z-bg: 0; --z-content: 5; --z-map: 10; --z-map-overlay: 20; --z-map-float: 30;
  --z-tooltip: 45; --z-header: 55; --z-mask: 65; --z-modal: 70; --z-notify: 90;
  --scrollbar-width: 6px; --scrollbar-track: transparent;
  --scrollbar-thumb: rgba(255, 215, 0, 0.25); --scrollbar-thumb-hover: rgba(255, 215, 0, 0.40);
  --spacing-unit: 4px;
  --duration-fast: 150ms; --duration-normal: 200ms; --duration-slow: 300ms;
  --duration-slower: 500ms; --duration-slowest: 800ms;
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1); --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1); --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ========== 暖橙数据风 ========== */
:root[data-theme="warm-orange"] {
  --bg-page: #1A1210;
  --bg-panel: rgba(50, 35, 15, 0.8);
  --bg-panel-solid: #1E1A14;
  --bg-card: rgba(40, 30, 15, 0.5);
  --border-panel: rgba(255, 140, 66, 0.3);
  --color-primary: #FF8C42;
  --color-primary-rgb: 255, 140, 66;
  --color-secondary: #FFB347;
  --color-accent: #FFD93D;
  --color-title: #FFFFFF;
  --color-panel-title: #FF8C42;
  --color-text: #FFF0E0;
  --color-text-muted: #8A7A6A;
  --color-highlight: #FFD93D;
  --color-warning: #FF6B6B;
  --glow-color: rgba(255, 140, 66, 0.6);
  --gradient-primary: linear-gradient(to top, #8A4500, #FF8C42);
  --gradient-secondary: linear-gradient(to top, #8A6A00, #FFB347);
  --gradient-area: linear-gradient(to bottom, rgba(255,140,66,0.3), transparent);
  --gradient-panel: linear-gradient(180deg, rgba(50,35,15,0.9), rgba(30,20,8,0.9));
  --gradient-glow-bar: linear-gradient(90deg, transparent, #FF8C42, transparent);
  --bg-title-bar: rgba(255, 140, 66, 0.15);
  --gradient-header-bg: linear-gradient(180deg, rgba(255,140,66,0.10), transparent);
  --gradient-header-glow: linear-gradient(90deg, transparent, #FF8C42, transparent);
  --gradient-title-text: linear-gradient(90deg, #FF8C42, #FFFFFF 50%, #FF8C42);
  --gradient-panel-title-text: linear-gradient(90deg, #FF8C42, #FFFFFF);
  --btn-primary-bg: linear-gradient(135deg, #FF8C42, #FFB347);
  --btn-primary-text: #FFFFFF;
  --btn-secondary-text: #FF8C42;
  --btn-secondary-border: rgba(255, 140, 66, 0.5);
  --btn-danger-bg: linear-gradient(135deg, #CC3333, #FF6B6B);
  --btn-hover-overlay: rgba(255, 255, 255, 0.15);
  --btn-active-overlay: rgba(0, 0, 0, 0.1);
  --btn-disabled-bg: rgba(255, 255, 255, 0.1);
  --btn-disabled-text: rgba(255, 255, 255, 0.3);
  --tab-capsule-bg: rgba(255, 140, 66, 0.08);
  --tab-active-bg: linear-gradient(135deg, #FF8C42, #FFB347);
  --shadow-panel: 0 2px 12px rgba(255,140,66,0.08);
  --shadow-hover: 0 4px 20px rgba(255,140,66,0.15);
  --shadow-card: 0 2px 8px rgba(255,140,66,0.06);
  --shadow-modal: 0 8px 32px rgba(255,140,66,0.2);
  --shadow-map-overlay: 0 4px 16px rgba(255,140,66,0.12);
  --badge-success: #52C41A; --badge-danger: #FF4D4F; --badge-warning: #FAAD14;
  --badge-info: #1890FF; --badge-completed: #52C41A; --badge-closed: rgba(255, 255, 255, 0.35);
  --z-bg: 0; --z-content: 5; --z-map: 10; --z-map-overlay: 20; --z-map-float: 30;
  --z-tooltip: 45; --z-header: 55; --z-mask: 65; --z-modal: 70; --z-notify: 90;
  --scrollbar-width: 6px; --scrollbar-track: transparent;
  --scrollbar-thumb: rgba(255, 140, 66, 0.25); --scrollbar-thumb-hover: rgba(255, 140, 66, 0.40);
  --spacing-unit: 4px;
  --duration-fast: 150ms; --duration-normal: 200ms; --duration-slow: 300ms;
  --duration-slower: 500ms; --duration-slowest: 800ms;
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1); --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1); --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ========== 紫蓝深邃风 ========== */
:root[data-theme="deep-purple"] {
  --bg-page: #0E0A20;
  --bg-panel: rgba(20, 16, 60, 0.8);
  --bg-panel-solid: #14103A;
  --bg-card: rgba(15, 10, 45, 0.5);
  --border-panel: rgba(168, 85, 247, 0.3);
  --color-primary: #A855F7;
  --color-primary-rgb: 168, 85, 247;
  --color-secondary: #6366F1;
  --color-accent: #C084FC;
  --color-title: #FFFFFF;
  --color-panel-title: #A855F7;
  --color-text: #E8E0FF;
  --color-text-muted: #7A6A8A;
  --color-highlight: #C084FC;
  --color-warning: #FF6B6B;
  --glow-color: rgba(168, 85, 247, 0.6);
  --gradient-primary: linear-gradient(to top, #3B0086, #A855F7);
  --gradient-secondary: linear-gradient(to top, #1A0086, #6366F1);
  --gradient-area: linear-gradient(to bottom, rgba(168,85,247,0.3), transparent);
  --gradient-panel: linear-gradient(180deg, rgba(20,16,60,0.9), rgba(10,8,40,0.9));
  --gradient-glow-bar: linear-gradient(90deg, transparent, #A855F7, transparent);
  --bg-title-bar: rgba(168, 85, 247, 0.15);
  --gradient-header-bg: linear-gradient(180deg, rgba(168,85,247,0.15), transparent);
  --gradient-header-glow: linear-gradient(90deg, transparent, #A855F7, transparent);
  --gradient-title-text: linear-gradient(90deg, #A855F7, #FFFFFF 50%, #A855F7);
  --gradient-panel-title-text: linear-gradient(90deg, #A855F7, #C084FC);
  --btn-primary-bg: linear-gradient(135deg, #6366F1, #A855F7);
  --btn-primary-text: #FFFFFF;
  --btn-secondary-text: #A855F7;
  --btn-secondary-border: rgba(168, 85, 247, 0.5);
  --btn-danger-bg: linear-gradient(135deg, #CC3333, #FF6B6B);
  --btn-hover-overlay: rgba(255, 255, 255, 0.15);
  --btn-active-overlay: rgba(0, 0, 0, 0.1);
  --btn-disabled-bg: rgba(255, 255, 255, 0.1);
  --btn-disabled-text: rgba(255, 255, 255, 0.3);
  --tab-capsule-bg: rgba(168, 85, 247, 0.08);
  --tab-active-bg: linear-gradient(135deg, #6366F1, #A855F7);
  --shadow-panel: 0 2px 12px rgba(168,85,247,0.08);
  --shadow-hover: 0 4px 20px rgba(168,85,247,0.15);
  --shadow-card: 0 2px 8px rgba(168,85,247,0.06);
  --shadow-modal: 0 8px 32px rgba(168,85,247,0.2);
  --shadow-map-overlay: 0 4px 16px rgba(168,85,247,0.12);
  --badge-success: #52C41A; --badge-danger: #FF4D4F; --badge-warning: #FAAD14;
  --badge-info: #1890FF; --badge-completed: #52C41A; --badge-closed: rgba(255, 255, 255, 0.35);
  --z-bg: 0; --z-content: 5; --z-map: 10; --z-map-overlay: 20; --z-map-float: 30;
  --z-tooltip: 45; --z-header: 55; --z-mask: 65; --z-modal: 70; --z-notify: 90;
  --scrollbar-width: 6px; --scrollbar-track: transparent;
  --scrollbar-thumb: rgba(168, 85, 247, 0.25); --scrollbar-thumb-hover: rgba(168, 85, 247, 0.40);
  --spacing-unit: 4px;
  --duration-fast: 150ms; --duration-normal: 200ms; --duration-slow: 300ms;
  --duration-slower: 500ms; --duration-slowest: 800ms;
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1); --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1); --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ========== 浅色商务风 ========== */
:root[data-theme="light-business"] {
  --bg-page: #F0F2F5;
  --bg-panel: rgba(255, 255, 255, 0.95);
  --bg-panel-solid: #FFFFFF;
  --bg-card: #FAFAFA;
  --border-panel: #E8E8E8;
  --color-primary: #1890FF;
  --color-primary-rgb: 24, 144, 255;
  --color-secondary: #52C41A;
  --color-accent: #FAAD14;
  --color-title: #262626;
  --color-panel-title: #1890FF;
  --color-text: #595959;
  --color-text-muted: #8C8C8C;
  --color-highlight: #1890FF;
  --color-warning: #FF4D4F;
  --glow-color: transparent;
  --gradient-primary: linear-gradient(to top, #096DD9, #1890FF);
  --gradient-secondary: linear-gradient(to top, #237804, #52C41A);
  --gradient-area: linear-gradient(to bottom, rgba(24,144,255,0.15), transparent);
  --gradient-panel: linear-gradient(180deg, #FFFFFF, #FAFAFA);
  --gradient-glow-bar: none;
  --bg-title-bar: #F0F5FF;
  --gradient-header-bg: linear-gradient(180deg, #FFFFFF, #F0F2F5);
  --gradient-header-glow: none;
  --gradient-title-text: none;
  --gradient-panel-title-text: none;
  --btn-primary-bg: #1890FF;
  --btn-primary-text: #FFFFFF;
  --btn-secondary-text: #1890FF;
  --btn-secondary-border: #1890FF;
  --btn-danger-bg: #FF4D4F;
  --btn-hover-overlay: rgba(255, 255, 255, 0.15);
  --btn-active-overlay: rgba(0, 0, 0, 0.1);
  --btn-disabled-bg: rgba(0, 0, 0, 0.04);
  --btn-disabled-text: rgba(0, 0, 0, 0.25);
  --tab-capsule-bg: #F0F0F0;
  --tab-active-bg: #1890FF;
  --shadow-panel: 0 2px 8px rgba(0,0,0,0.06);
  --shadow-hover: 0 4px 16px rgba(0,0,0,0.1);
  --shadow-card: 0 2px 6px rgba(0,0,0,0.04);
  --shadow-modal: 0 8px 24px rgba(0,0,0,0.15);
  --shadow-map-overlay: 0 4px 12px rgba(0,0,0,0.08);
  --badge-success: #52C41A; --badge-danger: #F5222D; --badge-warning: #FAAD14;
  --badge-info: #1890FF; --badge-completed: #52C41A; --badge-closed: rgba(0, 0, 0, 0.25);
  --z-bg: 0; --z-content: 5; --z-map: 10; --z-map-overlay: 20; --z-map-float: 30;
  --z-tooltip: 45; --z-header: 55; --z-mask: 65; --z-modal: 70; --z-notify: 90;
  --scrollbar-width: 6px; --scrollbar-track: rgba(0, 0, 0, 0.04);
  --scrollbar-thumb: rgba(0, 0, 0, 0.15); --scrollbar-thumb-hover: rgba(0, 0, 0, 0.25);
  --spacing-unit: 4px;
  --duration-fast: 150ms; --duration-normal: 200ms; --duration-slow: 300ms;
  --duration-slower: 500ms; --duration-slowest: 800ms;
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1); --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1); --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

---

## 八、使用方式

### 在 main.js 中引入

```javascript
import Vue from 'vue'
import App from './App.vue'
import ThemeProvider from '@/components/ThemeProvider.vue'

Vue.component('ThemeProvider', ThemeProvider)

new Vue({
  render: h => h(App),
}).$mount('#app')
```

### 在 App.vue 中使用

```vue
<template>
  <ThemeProvider :theme="currentTheme" @change="handleThemeChange">
    <Dashboard />
  </ThemeProvider>
</template>

<script>
export default {
  data() {
    return {
      currentTheme: 'techBlue', // 默认深蓝科技主题
    }
  },
  methods: {
    handleThemeChange(theme) {
      this.currentTheme = theme
    },
  },
}
</script>
```

### 向后兼容使用

```javascript
// 旧代码使用 darkTech 键名仍然有效
import { getTheme } from './themes/index'

getTheme('darkTech')    // 自动映射到 techBlue
getTheme('tourism')     // 自动映射到 ecoGreen
getTheme('lightBright') // 自动映射到 lightBusiness
getTheme('partyRed')    // 保持不变
```

---

## 触发词配置

在 SKILL.md 中增加主题触发词：

| 触发词 | 生成的主题 | cssKey |
|--------|------------|--------|
| 科技蓝大屏、深色大屏、科技大屏、智慧城市大屏、智慧乡村大屏（默认） | techBlue（深蓝科技） | tech-blue |
| 生态大屏、青绿大屏、水利大屏、农业大屏、碳排放大屏、文旅生态大屏 | ecoGreen（青绿生态） | eco-green |
| 党建红金大屏、党建大屏、政务大屏、廉政大屏 | partyRed（党建红金） | party-red |
| 暖橙大屏、经济大屏、产业大屏、GDP大屏、招商大屏 | warmOrange（暖橙数据） | warm-orange |
| 紫蓝大屏、数字孪生大屏、3D大屏、城市大脑大屏 | deepPurple（紫蓝深邃） | deep-purple |
| 浅色大屏、商务大屏、白色大屏、报表大屏、企业大屏 | lightBusiness（浅色商务） | light-business |

### 主题选型速查表

| 你要做什么大屏 | 推荐主题 |
|--------------|---------|
| 智慧乡村/社区总览 | techBlue（深蓝科技） |
| 生态/水利/农业 | ecoGreen（青绿生态） |
| 党建/政务/廉政 | partyRed（党建红金） |
| 经济/产业/GDP | warmOrange（暖橙数据） |
| 数字孪生/3D/城市大脑 | deepPurple（紫蓝深邃） |
| 企业报表/会议室/移动端 | lightBusiness（浅色商务） |
