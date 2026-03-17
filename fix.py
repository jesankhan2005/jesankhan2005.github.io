content = open('index.html', 'r').read()
old = '''      <div class="project-body">
            <div class="project-card">
      <div class="project-header">
        <span class="project-icon">💬</span>
        <div class="project-links">
          <a href="https://jesankhan2005-whatsapp-chat-analyzer.streamlit.app" target="_blank">Live</a>
          <a href="https://github.com/jesankhan2005/whatsapp-chat-analyzer" target="_blank">GitHub</a>
        </div>
      </div>
      <div class="project-body">
        <h3>WhatsApp Chat Analyzer</h3>
        <p>Analyze WhatsApp chats \u2014 messages, timelines, word cloud, emoji analysis and more!</p>
        <div class="project-tags">
          <span class="tag">Python</span>
          <span class="tag">Streamlit</span>
          <span class="tag">NLP</span>
          <span class="tag">Pandas</span>
        </div>
      </div>
    </div>
    <h3>IPL Cricket SQL Analysis</h3>'''

new = '''      <div class="project-body">
        <h3>IPL Cricket SQL Analysis</h3>'''

content = content.replace(old, new, 1)
open('index.html', 'w').write(content)
print('Done!')
