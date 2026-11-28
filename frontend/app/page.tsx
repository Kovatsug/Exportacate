export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-8">
      <div className="max-w-2xl w-full text-center space-y-8">
        <div className="space-y-4">
          <h1 className="text-4xl md:text-6xl font-bold text-primary-700">
            Exportacate
          </h1>
          <p className="text-xl text-gray-600">
            Sistema de gestão para exportação de abacates
          </p>
          <p className="text-lg text-gray-500">
            Do pomar ao pagamento — controle completo do ciclo de exportação
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
          <div className="p-6 bg-white rounded-xl shadow-md border border-gray-100">
            <h2 className="text-lg font-semibold text-gray-800 mb-2">Backend API</h2>
            <p className="text-gray-600 text-sm">
              Flask + SQLAlchemy + PostgreSQL/MySQL
              <br />
              <span className="text-primary-600 font-mono">http://localhost:5000</span>
            </p>
          </div>
          <div className="p-6 bg-white rounded-xl shadow-md border border-gray-100">
            <h2 className="text-lg font-semibold text-gray-800 mb-2">Frontend</h2>
            <p className="text-gray-600 text-sm">
              Next.js 14 + React 18 + Tailwind CSS
              <br />
              <span className="text-primary-600 font-mono">http://localhost:3000</span>
            </p>
          </div>
          <div className="p-6 bg-white rounded-xl shadow-md border border-gray-100">
            <h2 className="text-lg font-semibold text-gray-800 mb-2">Documentação</h2>
            <p className="text-gray-600 text-sm">
              Minimundo: <code>docs/miniworld.md</code>
              <br />
              Arquitetura: <code>docs/architecture.md</code>
            </p>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-gray-200">
          <p className="text-sm text-gray-500">
            Projeto da disciplina de Desenvolvimento Web (AV6) — IFC
          </p>
        </div>
      </div>
    </main>
  )
}