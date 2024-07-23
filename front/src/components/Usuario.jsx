

export const Usuario = ({id,nombre,apellido,dni}) => {

	let idRoute = `client${id-1}`
	return(
		<article className="flex gap-2">
			<a href={idRoute} className="text-slate-50">{id}</a>
			<h1 className="text-slate-50">{nombre}</h1>
			<h1 className="text-slate-50">{apellido}</h1>
			<h1 className="text-slate-50">{dni}</h1>
		</article>
		
	)
}

