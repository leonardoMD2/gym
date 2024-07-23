

export const UsuarioEditable = ({nombre,apellido,dni}) => {

	return(
		<article className="flex gap-2">
			<h1 className="text-slate-50">{nombre}</h1>
			<h1 className="text-slate-50">{apellido}</h1>
			<h1 className="text-slate-50">{dni}</h1>
		</article>
		
	)
}

