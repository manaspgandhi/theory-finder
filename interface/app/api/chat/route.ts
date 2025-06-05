// app/api/chat/route.ts
export async function POST(req: Request) {
  const { message } = await req.json();

  // Mocked GPT reply — replace this with OpenAI call if needed
  const reply = `You said: "${message}"`;

  return new Response(JSON.stringify({ reply }), {
    headers: { "Content-Type": "application/json" },
  });
}
