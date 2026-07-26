// AI Knowledge Assistant Widget (9router Integration)
(function () {
  const DEFAULT_SETTINGS = {
    endpoint: "http://localhost:3000/v1", // Default 9router proxy endpoint
    apiKey: "",
    model: "gemini-2.0-flash"
  };

  function getSettings() {
    try {
      const saved = localStorage.getItem("ai_chat_settings");
      return saved ? { ...DEFAULT_SETTINGS, ...JSON.parse(saved) } : DEFAULT_SETTINGS;
    } catch (e) {
      return DEFAULT_SETTINGS;
    }
  }

  function saveSettings(settings) {
    localStorage.setItem("ai_chat_settings", JSON.stringify(settings));
  }

  function initWidget() {
    if (document.getElementById("ai-chat-fab")) return;

    // Create FAB
    const fab = document.createElement("button");
    fab.id = "ai-chat-fab";
    fab.className = "ai-chat-fab";
    fab.innerHTML = `<span>🤖</span> <span>Ask AI</span>`;
    document.body.appendChild(fab);

    // Create Drawer
    const drawer = document.createElement("div");
    drawer.id = "ai-chat-drawer";
    drawer.className = "ai-chat-drawer";
    drawer.innerHTML = `
      <div class="ai-chat-header">
        <div class="ai-chat-title">
          <span>🤖</span> Knowledge AI Assistant
        </div>
        <div class="ai-chat-header-actions">
          <button class="ai-chat-icon-btn" id="ai-chat-settings-toggle" title="Settings">⚙️</button>
          <button class="ai-chat-icon-btn" id="ai-chat-close" title="Close">✕</button>
        </div>
      </div>

      <div class="ai-chat-settings" id="ai-chat-settings-panel">
        <div class="ai-chat-field">
          <label class="ai-chat-label">9router / LLM Proxy Endpoint</label>
          <input type="text" class="ai-chat-input-field" id="ai-setting-endpoint" placeholder="http://localhost:3000/v1" />
        </div>
        <div class="ai-chat-field">
          <label class="ai-chat-label">API Key (Optional if 9router proxy)</label>
          <input type="password" class="ai-chat-input-field" id="ai-setting-apikey" placeholder="sk-..." />
        </div>
        <div class="ai-chat-field">
          <label class="ai-chat-label">Model</label>
          <input type="text" class="ai-chat-input-field" id="ai-setting-model" placeholder="gemini-2.0-flash" />
        </div>
        <button class="ai-chat-send-btn" id="ai-setting-save" style="padding: 8px; margin-top: 6px;">Save Settings</button>
      </div>

      <div class="ai-chat-body" id="ai-chat-messages">
        <div class="ai-chat-msg assistant">
          👋 Xin chào! Tôi là AI Assistant của Knowledge Space. Bạn có thể hỏi tôi bất kỳ thông tin nào có trên website này.
        </div>
      </div>

      <div class="ai-chat-input-area">
        <input type="text" class="ai-chat-input" id="ai-chat-input-text" placeholder="Hỏi về BIM ISO, AI Research, Trading..." />
        <button class="ai-chat-send-btn" id="ai-chat-send">Gửi</button>
      </div>
    `;
    document.body.appendChild(drawer);

    // Load Settings
    const settings = getSettings();
    document.getElementById("ai-setting-endpoint").value = settings.endpoint;
    document.getElementById("ai-setting-apikey").value = settings.apiKey;
    document.getElementById("ai-setting-model").value = settings.model;

    // Toggle Events
    fab.addEventListener("click", () => drawer.classList.toggle("open"));
    document.getElementById("ai-chat-close").addEventListener("click", () => drawer.classList.remove("open"));

    const settingsPanel = document.getElementById("ai-chat-settings-panel");
    const messagesPanel = document.getElementById("ai-chat-messages");
    document.getElementById("ai-chat-settings-toggle").addEventListener("click", () => {
      if (settingsPanel.classList.contains("active")) {
        settingsPanel.classList.remove("active");
        messagesPanel.style.display = "flex";
      } else {
        settingsPanel.classList.add("active");
        messagesPanel.style.display = "none";
      }
    });

    document.getElementById("ai-setting-save").addEventListener("click", () => {
      saveSettings({
        endpoint: document.getElementById("ai-setting-endpoint").value.trim(),
        apiKey: document.getElementById("ai-setting-apikey").value.trim(),
        model: document.getElementById("ai-setting-model").value.trim()
      });
      settingsPanel.classList.remove("active");
      messagesPanel.style.display = "flex";
      appendMessage("assistant", "⚙️ Đã lưu cấu hình kết nối!");
    });

    // Send Message
    const inputEl = document.getElementById("ai-chat-input-text");
    const sendBtn = document.getElementById("ai-chat-send");

    async function handleSend() {
      const text = inputEl.value.trim();
      if (!text) return;
      inputEl.value = "";
      appendMessage("user", text);

      // Extract Context from active page
      let contextText = "";
      const pageArticle = document.querySelector("article");
      if (pageArticle) {
        contextText = pageArticle.innerText.substring(0, 3000);
      }

      const assistantMsgEl = appendMessage("assistant", "🔍 Đang truy vấn tri thức & phản hồi...");

      try {
        const curSettings = getSettings();
        const endpointUrl = curSettings.endpoint.replace(/\/$/, "") + "/chat/completions";
        
        const response = await fetch(endpointUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...(curSettings.apiKey ? { Authorization: `Bearer ${curSettings.apiKey}` } : {})
          },
          body: JSON.stringify({
            model: curSettings.model || "gemini-2.0-flash",
            messages: [
              {
                role: "system",
                content: `You are an intelligent knowledge base assistant. Answer the user's question accurately based on the current website article context if provided:\n\n=== ARTICLE CONTEXT ===\n${contextText}\n=====================`
              },
              { role: "user", content: text }
            ],
            stream: false
          })
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();
        const reply = data.choices?.[0]?.message?.content || "Không có phản hồi từ model.";
        assistantMsgEl.innerHTML = reply.replace(/\n/g, "<br/>");
      } catch (err) {
        assistantMsgEl.innerHTML = `⚠️ Không thể kết nối AI Provider (${err.message}). Vui lòng kiểm tra lại cấu hình Endpoint (9router / API Key) trong phần ⚙️ Settings.`;
      }
    }

    sendBtn.addEventListener("click", handleSend);
    inputEl.addEventListener("keypress", (e) => {
      if (e.key === "Enter") handleSend();
    });
  }

  function appendMessage(role, text) {
    const container = document.getElementById("ai-chat-messages");
    const msg = document.createElement("div");
    msg.className = `ai-chat-msg ${role}`;
    msg.innerHTML = text.replace(/\n/g, "<br/>");
    container.appendChild(msg);
    container.scrollTop = container.scrollHeight;
    return msg;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initWidget);
  } else {
    initWidget();
  }
})();
