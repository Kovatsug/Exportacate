import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Exportacate - Gestão de Exportação de Abacates',
  description: 'Sistema de gestão para exportação de abacates: do pomar ao pagamento',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  )
}