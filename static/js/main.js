document.addEventListener('DOMContentLoaded', () => {
    // --- Navigation & Views ---
    const navItems = document.querySelectorAll('.nav-item');
    const viewSections = document.querySelectorAll('.view-section');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            // Remove active class from all
            navItems.forEach(nav => nav.classList.remove('active'));
            viewSections.forEach(section => {
                section.classList.remove('active');
                setTimeout(() => { if (!section.classList.contains('active')) section.style.display = 'none'; }, 300);
            });

            // Add active class to clicked
            item.classList.add('active');
            const targetId = item.getAttribute('data-target');
            const targetElem = document.getElementById(targetId);
            targetElem.style.display = 'flex';
            setTimeout(() => targetElem.classList.add('active'), 10);
        });
    });

    // --- Theme Toggle ---
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElem = document.documentElement;
    const themeIcon = themeToggle.querySelector('i');
    const themeText = themeToggle.querySelector('span');

    // Check local storage for theme
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);

    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlElem.getAttribute('data-theme') || 'dark';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });

    function setTheme(theme) {
        htmlElem.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        if (theme === 'light') {
            themeIcon.className = 'fa-solid fa-sun';
            themeText.textContent = 'Light Mode';
        } else {
            themeIcon.className = 'fa-solid fa-moon';
            themeText.textContent = 'Dark Mode';
        }
    }

    // --- Chat Logic (Ask Vakil Sahab) ---
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = chatInput.value.trim();
        if (!query) return;

        // Add user message
        appendMessage(chatMessages, query, 'user');
        chatInput.value = '';

        // Add loading indicator
        const loadingId = appendLoading(chatMessages);
        
        try {
            const response = await fetch(`/api/v1/chat/ask_vakil_sahab?user_query=${encodeURIComponent(query)}`, {
                method: 'POST'
            });
            const data = await response.json();
            
            removeLoading(loadingId);
            // Assuming response returns string directly or obj with data
            const reply = typeof data === 'string' ? data : (data.answer || data.response || JSON.stringify(data));
            appendMessage(chatMessages, reply, 'system');
            
        } catch (error) {
            removeLoading(loadingId);
            appendMessage(chatMessages, 'Sorry, I encountered an error. Please try again later.', 'system');
            console.error(error);
        }
    });

    // --- Agent Logic (MCP Agent) ---
    const agentForm = document.getElementById('agent-form');
    const agentInput = document.getElementById('agent-input');
    const agentMessages = document.getElementById('agent-messages');

    agentForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = agentInput.value.trim();
        if (!query) return;

        appendMessage(agentMessages, query, 'user');
        agentInput.value = '';

        const loadingId = appendLoading(agentMessages);
        
        try {
            const response = await fetch(`/api/v1/chat_mcp_agent/chat_agent?query=${encodeURIComponent(query)}`, {
                method: 'POST'
            });
            const data = await response.json();
            
            removeLoading(loadingId);
            
            let reply = "I'm sorry, I couldn't understand the response.";
            
            if (data.data && data.data.messages && data.data.messages.length > 0) {
                // The last message is usually the AIMessage
                const lastMsg = data.data.messages[data.data.messages.length - 1];
                if (typeof lastMsg === 'object' && lastMsg.content) {
                    if (typeof lastMsg.content === 'string') {
                        reply = lastMsg.content;
                    } else if (Array.isArray(lastMsg.content)) {
                         // Sometimes it's an array of mixed blocks
                         reply = lastMsg.content.map(c => c.text || JSON.stringify(c)).join('\n');
                    }
                } else {
                     reply = JSON.stringify(lastMsg);
                }
            } else if (data.data) {
                reply = typeof data.data === 'string' ? data.data : JSON.stringify(data.data);
            } else if (data.response) {
                reply = typeof data.response === 'string' ? data.response : JSON.stringify(data.response);
            } else {
                 reply = JSON.stringify(data);
            }
            
            appendMessage(agentMessages, reply, 'system');
            
        } catch (error) {
            removeLoading(loadingId);
            appendMessage(agentMessages, 'Error communicating with MCP Agent.', 'system');
            console.error(error);
        }
    });

    // --- Helper Functions for Chat Setup ---
    function appendMessage(container, text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}-message`;
        
        let iconClass = sender === 'user' ? 'fa-solid fa-user' : 'fa-solid fa-scale-balanced';
        if (container.id === 'agent-messages' && sender === 'system') iconClass = 'fa-solid fa-robot';

        // Parse markdown for system messages
        const formattedText = sender === 'system' ? marked.parse(text) : text;
        const bubbleContent = sender === 'system' ? formattedText : `<p>${escapeHTML(text)}</p>`;

        msgDiv.innerHTML = `
            <div class="avatar"><i class="${iconClass}"></i></div>
            <div class="bubble">${bubbleContent}</div>
        `;
        container.appendChild(msgDiv);
        
        // Auto-scroll
        const scrollContainer = container.parentElement;
        scrollContainer.scrollTop = scrollContainer.scrollHeight;
    }

    function appendLoading(container) {
        const id = 'loading-' + Date.now();
        const msgDiv = document.createElement('div');
        msgDiv.className = 'message system-message';
        msgDiv.id = id;
        
        let iconClass = 'fa-solid fa-scale-balanced';
        if (container.id === 'agent-messages') iconClass = 'fa-solid fa-robot';

        msgDiv.innerHTML = `
            <div class="avatar"><i class="${iconClass}"></i></div>
            <div class="bubble">
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        `;
        container.appendChild(msgDiv);
        
        const scrollContainer = container.parentElement;
        scrollContainer.scrollTop = scrollContainer.scrollHeight;
        
        return id;
    }

    function removeLoading(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }

    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g, 
            tag => ({
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                "'": '&#39;',
                '"': '&quot;'
            }[tag] || tag)
        );
    }

    // --- Legal Web Search Logic ---
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    const searchLoader = document.getElementById('search-loader');

    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = searchInput.value.trim();
        if (!query) return;

        // Clear previous and show loader
        searchResults.innerHTML = '';
        searchResults.style.display = 'none';
        searchLoader.style.display = 'flex';

        try {
            const response = await fetch(`/api/v1/search/legal_web_search?query=${encodeURIComponent(query)}&max_results=5`);
            const data = await response.json();
            
            searchLoader.style.display = 'none';
            searchResults.style.display = 'flex';
            
            // Expected data format from previous checks: likely a string or object.
            // If it returns a string, we might just display it as markdown.
            // If it returns a list of items, we map them. 
            // In graph_call, the tool often returns markdown summarizing the search.
            
            if (typeof data === 'string') {
                searchResults.innerHTML = `<div class="result-card"><div class="result-snippet">${marked.parse(data)}</div></div>`;
            } else if (data.results && Array.isArray(data.results)) {
                if (data.results.length === 0) {
                    searchResults.innerHTML = `<div class="empty-state"><p>No results found.</p></div>`;
                } else {
                    data.results.forEach(item => {
                        const div = document.createElement('div');
                        div.className = 'result-card';
                        div.innerHTML = `
                            <a href="${item.url || '#'}" target="_blank" class="result-title">${escapeHTML(item.title || 'Result')}</a>
                            ${item.url ? `<div class="result-url"><i class="fa-solid fa-link"></i> ${escapeHTML(item.url)}</div>` : ''}
                            <div class="result-snippet">${escapeHTML(item.content || item.snippet || '')}</div>
                        `;
                        searchResults.appendChild(div);
                    });
                }
            } else {
                // dump as JSON/markdown if structure is unknown
                const content = data.response || data.data || JSON.stringify(data);
                searchResults.innerHTML = `<div class="result-card"><div class="result-snippet">${marked.parse(typeof content === 'string' ? content : JSON.stringify(content))}</div></div>`;
            }

        } catch (error) {
            searchLoader.style.display = 'none';
            searchResults.style.display = 'flex';
            searchResults.innerHTML = `<div class="empty-state" style="color: #ef4444;"><i class="fa-solid fa-circle-exclamation"></i><p>Error fetching search results.</p></div>`;
            console.error(error);
        }
    });

    // --- Legal Case Predictor Logic ---
    const predictForm = document.getElementById('predict-form');
    const predictResultCard = document.getElementById('predict-result');
    const probValue = document.getElementById('prob-value');
    const strengthValue = document.getElementById('strength-value');

    if (predictForm) {
        predictForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const payload = {
                case_type: parseInt(document.getElementById('case_type').value),
                lawyer_exp: parseFloat(document.getElementById('lawyer_exp').value),
                judge_exp: parseFloat(document.getElementById('judge_exp').value),
                judge_count: parseInt(document.getElementById('judge_count').value)
            };

            const submitBtn = predictForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<div class="spinner" style="width: 16px; height: 16px; border-width: 2px;"></div> Calculating...';
            submitBtn.disabled = true;
            predictResultCard.style.display = 'none';

            try {
                const response = await fetch('/api/v1/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    probValue.textContent = data.win_probability + '%';
                    strengthValue.textContent = data.case_strength;
                    
                    // Reset classes
                    strengthValue.className = 'badge ' + data.case_strength.toLowerCase();

                    predictResultCard.style.display = 'block';
                } else {
                    alert("Error calculating probability: " + (data.error || "Unknown error"));
                }
            } catch (error) {
                console.error("Prediction failed:", error);
                alert("Could not connect to the server for prediction.");
            } finally {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }
        });
    }

});
