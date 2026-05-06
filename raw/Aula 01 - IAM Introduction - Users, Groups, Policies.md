[[Módulo 02 - IAM & AWS CLI]]

IAM significa identidade e gestão de acesso. Esse serviço server para criar os usuários e atribui-los a um grupo.
Ao criar uma conta na AWS, é criado uma conta raiz. Com esse serviço criamos usuários, que fazem parte da organização. Sendo possível agrupa-los.

![[Pasted image 20260506065230.png]]

Nesse exemplo acima, temos dois grupos de usuários.

> OBS: Um grupo só pode conter usuários, e não outro grupo

Como visto no exemplo acima, um usuário pode não pertencer a um grupo, mesmo não sendo uma pratica comum e nem recomendada.

![[Pasted image 20260506065550.png]]

É possível criar grupos com usuários já atribuídos a outros grupos.

É atribuído a um grupo e/ou usuário, por meio de `policies`.  `Policies` são objetos JSON com configurações de permissionamento dentro da organização.

![[Pasted image 20260506070037.png]]

Uma pratica comum na AWS é aplicar o princípio de menor privilégio. Isso significa, dar o mínimo de privilégio possível ao usuário, apenas o necessário.

