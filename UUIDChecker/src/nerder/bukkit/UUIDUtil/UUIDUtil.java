/**
 * 
 */
/**
 * @author Nerder
 *
 */
package nerder.bukkit.UUIDUtil;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;

import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.permissions.Permission;
import org.bukkit.plugin.PluginManager;
import org.bukkit.plugin.java.JavaPlugin;

public class UUIDUtil extends JavaPlugin implements Listener {
	
	public Permission PlayerBan = new Permission("UUIDUtil.PlayerBan");
	public Permission PlayerCheck = new Permission("UUIDUtil.PlayerCheck");
	public Permission FormatEdit = new Permission("UUIDUtil.FormatEdit");
	public Permission UnBannable = new Permission("UUIDUtil.UnBannable");
	
	@Override
	public void onEnable() {
		PluginManager pm = getServer().getPluginManager();
		pm.addPermission(PlayerCheck);
		pm.addPermission(PlayerBan);
		pm.addPermission(FormatEdit);
		pm.addPermission(UnBannable);
	    ArrayList<String> IDs = new ArrayList<String>();
	    getConfig().addDefault("Banlist", IDs);
	    getConfig().addDefault("Kick_Prefix","Your UUID Has Been Banned For: " );
	    getConfig().addDefault("BanFormat", ChatColor.DARK_RED+"!"+ChatColor.GOLD+"'s UUID has been banned for: "+ChatColor.GREEN+"@"+ChatColor.GOLD+" UUID: "+ChatColor.WHITE+"#");
	    getConfig().addDefault("CheckFormat", ChatColor.DARK_RED+"!" +ChatColor.GOLD+"'s Past Names:");
		getConfig().addDefault("UnbanFormat", ChatColor.DARK_RED + "!" + ChatColor.GOLD + "'s UUID Has Been Unbanned");
		getConfig().addDefault("UnbanWReasonFormat", ChatColor.DARK_RED +  "!" + ChatColor.GOLD + "'s UUID Has Been Unbanned For reason " + ChatColor.GREEN + "@");
		getConfig().addDefault("BanReasonFormat",ChatColor.GOLD+"!" + ChatColor.WHITE+"'s UUID Is Curently Banned For: "+ ChatColor.GREEN + "@");
		getConfig().addDefault("PastBanReasonFormat",ChatColor.DARK_RED+ "!" + ChatColor.GOLD+"'s UUID Used To Be Banned For: "+ ChatColor.GREEN+ "@" + ChatColor.GOLD+"But They Where Unbanned");
		getConfig().addDefault("UnbanReasonFormat",ChatColor.DARK_RED+"!"+ChatColor.GOLD+"'s UUID Was Unbanned For: "+ ChatColor.GREEN+"@");
		getConfig().addDefault("NotBannedFormat",ChatColor.DARK_RED+"!"+ChatColor.GOLD+"'s UUID Has Never Been Banned");
	    getConfig().options().copyDefaults(true);
	    saveConfig();
		getLogger().info(" ");
		System.out.println("Penguin Slapper Initialized");
		getServer().getPluginManager().registerEvents(this, this);
	    getLogger().info("[CoreStats] Has been enabled!");
	    updateBans();
	}
	
	@Override
	public void onDisable() {
		
	}

	public void updateBans() {
		ArrayList<String> list = (ArrayList<String>) getConfig().getStringList("Banlist");
		if(list.size() > 0) {
			System.out.println("Ban list: "+list);
			for(int i = 1; i<list.size();i++) {
				String[] names = getNames(list.get(i).toString());
				for(int j = 0; j<names.length; j++) {
					getConfig().set("Banned_UUIDs." + list.get(i) + ".Banned Names", names[j]);
					if(!getConfig().isSet("Banned_Names."+ names[j])) {
						getConfig().set("Banned_UUIDs." + list.get(i) + ".Banned Names", names[j]);
					}
					saveConfig();
				}
			}	
		}
	}
	
	public String getUuid(String targetPlayer) {
		String uuid  = null;
		String output = null;
		try {
			if(getConfig().getString("Banned_Names."+targetPlayer) != null) {
				uuid = getConfig().getString("Banned_Names."+targetPlayer);
				return uuid;
			}
			System.out.println("Calling API at: "+"https://api.mojang.com/users/profiles/minecraft/"+ targetPlayer);
			URL url = new URL("https://api.mojang.com/users/profiles/minecraft/"+ targetPlayer);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setConnectTimeout(5000);
			conn.setRequestMethod("GET");
			conn.setRequestProperty("Accept", "application/json");
			if (conn.getResponseCode() != 200) {
				return "failed...\\";
			}
			BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
			System.out.println("Calling Mojang uuid API.../");
			output = br.readLine();
			conn.disconnect();
			} 
			catch (MalformedURLException e) {
			e.printStackTrace();
			}
		  	catch (IOException e) {
			e.printStackTrace();
			}
		String[] subSt = output.split("\"");
		uuid = subSt[3];
		return uuid;
	}
	
	public void dynMessage(CommandSender sender, String string) {
		if(sender instanceof Player) {
			Player player = (Player) sender;
			player.sendMessage(string);
		}
		System.out.println(ChatColor.stripColor(string));
	}
	
	public String[] getNames(String uuid) {
		String names = null;
		try {
			System.out.println("Calling API at: "+"https://api.mojang.com/user/profiles/"+uuid+"/names");
			URL url = new URL("https://api.mojang.com/user/profiles/"+uuid+"/names");
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setConnectTimeout(5000);
			conn.setRequestMethod("GET");
			conn.setRequestProperty("Accept", "application/json");

			if (conn.getResponseCode() != 200) {
				throw new RuntimeException("Failed : HTTP error code : "
						+ conn.getResponseCode());
			}

			BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
			System.out.println("Calling Mojang uuid API.../");
			names = br.readLine();
			conn.disconnect();
			} 
			catch (MalformedURLException e) {
			e.printStackTrace();
			} 
			catch (IOException e) {
			e.printStackTrace();
			}
		names = names.replace("[","");
		names = names.replace("]","");
		names = names.replaceAll("\\{\"name\":\"","");
		names = names.replace("}","");
		names = names.replaceAll("\"","");
		String[] namesArt = names.split(",");
		int g = 0;
		String[] namesArr = new String[namesArt.length];
		for(int i = 0; i<namesArt.length; i++) {
			if(!namesArt[i].contains("changedToAt")) {
				namesArr[g] = namesArt[i];
				g++;
			}
		}
		return namesArr;
	}
	
	public void NameCheck(CommandSender sender, String targetPlayer) {
        String uuid = getUuid(targetPlayer);
        if (uuid == "failed...\\") {
        	dynMessage(sender,"Invalid Username");
        }
        String[] names = getNames(uuid);
        dynMessage(sender,ChatColor.GOLD+"--------");
        dynMessage(sender,getFormat("CheckFormat",targetPlayer,"",""));
        int g=0;
        for(int i = 0; i<=names.length-1;i++) {
        	if(names[i] != null) {
        		dynMessage(sender,ChatColor.GOLD +""+ (g+1)+" - "+ChatColor.DARK_RED+names[i]);
        		g++;
        	}
        }
	}
	
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {	
		if (cmd.getName().equalsIgnoreCase("uuid") && sender instanceof Player) {
			playerCMDSwitch(sender, cmd, label, args);
		}
		else if (cmd.getName().equalsIgnoreCase("uuid") && !(sender instanceof Player)) {
			consoleCMDSwitch(sender,cmd,label,args);
		}
		saveConfig();
		return true;
	}
	
	public boolean playerCMDSwitch(CommandSender sender, Command cmd, String label, String[] args) {
		Player player = (Player) sender;
		if (!player.hasPermission(PlayerCheck)||!player.hasPermission(PlayerBan) || !player.hasPermission(FormatEdit) ){
		
			dynMessage(sender,ChatColor.DARK_RED+"I'm sorry, but you do not have permission to perform this command."
					+ " Please contact the server administrators if you believe that this is an error");
			return true;
		}
		
		if(args.length==0) {
			dynMessage(sender,"Use "+ChatColor.GOLD+"//uuid Help"+ChatColor.WHITE+"  - For help");
			return true;
		}
		String argument = args[0];
		
		if(argument.equalsIgnoreCase("Help") && (player.hasPermission(PlayerCheck))) {
			if(player.hasPermission(PlayerCheck)) {
			dynMessage(sender,ChatColor.GOLD + "/uuid Check (Username)" + ChatColor.WHITE + " -Returns past usernames");
			dynMessage(sender,ChatColor.GOLD + "/uuid Bancheck (Username)" + ChatColor.WHITE + " -Checks A Player's uuid For Past Or Current uuid Bans");
			}
			if(player.hasPermission(PlayerBan)) {
			dynMessage(sender,ChatColor.GOLD + "/uuid Ban (Username)(Reason)" + ChatColor.WHITE + " -Bans A Players uuid From The Server");
			dynMessage(sender,ChatColor.GOLD + "/uuid Unban (Username) (Optional Reason)" + ChatColor.WHITE + " -Unbans A Players uuid From The Server");
			}
			if (player.hasPermission(FormatEdit)){
			dynMessage(sender,ChatColor.GOLD + "/uuid Config" + ChatColor.WHITE + " -A Set Of Commands To Change Plugin Setings \"/uuid Config Help\" For More Info");
			}
		}
		else if(argument.equalsIgnoreCase("Check") && args.length >= 2 && player.hasPermission(PlayerCheck)) {
			NameCheck(sender,args[1]);
		}
		else if(argument.equalsIgnoreCase("Check") && args.length < 2 && player.hasPermission(PlayerCheck)) {
			dynMessage(sender,"Usage: "+ChatColor.GOLD+"/uuid Check (Username)");
		}
		else if(argument.equalsIgnoreCase("Ban") && args.length >= 3 && player.hasPermission(PlayerBan)) {
			ban(args);
		}
		else if(argument.equalsIgnoreCase("Ban") && args.length < 3 && player.hasPermission(PlayerBan)) {
			dynMessage(sender,"Usage: "+ChatColor.GOLD+"/uuid Ban (Username) (reason)");
		}
		else if(argument.equalsIgnoreCase("unban") && args.length >= 2 && player.hasPermission(PlayerBan)) {
			unBan(player, args);
		}
		else if(argument.equalsIgnoreCase("unban") && args.length < 2 && player.hasPermission(PlayerBan)) {
			dynMessage(sender,"Usage: "+ChatColor.GOLD+"/uuid unban (Username) (Optional Reason)");
		}
		else if(argument.equalsIgnoreCase("BanCheck") && args.length >= 2 && player.hasPermission(PlayerCheck)) {
			String uuid = getUuid(args[1]);
			Boolean isBanned = banCheck(args);
			if (isBanned) {
				String reason = getBanReason(args);
				dynMessage(sender,getFormat("BanReasonFormat",args[1],reason,""));
			}
			else if (!isBanned) {
				if(!getConfig().isSet("Banned_UUIDs."+uuid)) {
					dynMessage(sender,getFormat("NotBannedFormat",args[1],"",""));
				}
				if(getConfig().isSet("Banned_UUIDs." + uuid + ".Reason")) {
					String reason = getBanReason(args);
					dynMessage(sender,getFormat("PastBanReasonFormat",args[1],reason,""));
				}
				if(getConfig().isSet("Banned_UUIDs." + uuid + ".UnbanReason")) {
					String unbanReason = getUnbanReason(args);
					dynMessage(sender,getFormat("UnbanReasonFormat",args[1],unbanReason,""));
				}	
			}
		}
		else if(argument.equalsIgnoreCase("BanCheck") && args.length < 2 && player.hasPermission(PlayerCheck)) {
			dynMessage(sender,"Usage: "+ChatColor.GOLD+"/uuid config (Username)");
		}
		else if(argument.equalsIgnoreCase("Config") && args.length >= 2 && player.hasPermission(FormatEdit)) {
			configSwitch(sender, args);
		}
		else if(argument.equalsIgnoreCase("Config") && args.length < 2 && player.hasPermission(FormatEdit)) {
			dynMessage(sender,"Usage: "+ChatColor.GOLD+"/uuid config (Setting) (Option)");
			
		}
		else if(player.hasPermission(PlayerCheck)||player.hasPermission(PlayerBan) || player.hasPermission(FormatEdit) ) {
			dynMessage(sender,"Use "+ChatColor.GOLD+"/uuid Help"+ChatColor.WHITE+"  - For help");
		}
		
		else {
			dynMessage(sender,ChatColor.RED+"I'm sorry, but you do not have permission to perform this command."
					+ " Please contact the server administrators if you believe that this is an error");
		}
		return true;
	}
	
	public boolean consoleCMDSwitch(CommandSender sender, Command cmd, String label, String[] args) {
		
		if(args.length==0) {
			System.out.println("Use: //uuid Help - For help");
			return true;
		}
		String argument = args[0];
		
		if(argument.equalsIgnoreCase("Help")) {
			System.out.println("/uuid Check (Username) - Returns past usernames");
			System.out.println("/uuid Bancheck (Username) - Checks A Player's uuid For Past Or Current uuid Bans");
			System.out.println("/uuid Ban (Username)(Reason) - Bans A Players uuid From The Server");
			System.out.println("/uuid Unban (Username) (Optional Reason) - Unbans A Players uuid From The Server");
			System.out.println("/uuid Config - A Set Of Commands To Change Plugin Setings \"/uuid Config Help\" For More Info");
			
		}
		else if(argument.equalsIgnoreCase("Check") && args.length >= 2) {
			NameCheck(sender, args[1]);
		}
		else if(argument.equalsIgnoreCase("Check") && args.length < 2) {
			System.out.println("Usage: /uuid Check (Username)");
		}
		else if(argument.equalsIgnoreCase("Ban") && args.length >= 3) {
			ban(args);
		}
		else if(argument.equalsIgnoreCase("Ban") && args.length < 3) {
			System.out.println("Usage: /uuid Ban (Username) (reason)");
		}
		else if(argument.equalsIgnoreCase("unban") && args.length >= 2) {
			unBan(sender,args);
		}
		else if(argument.equalsIgnoreCase("unban") && args.length < 2) {
			System.out.println("Usage: /uuid unban (Username) (Optional Reason)");
		}
		else if(argument.equalsIgnoreCase("BanCheck") && args.length >= 2) {
			String uuid = getUuid(args[1]);
			Boolean isBanned = banCheck(args);
			if (isBanned == true) {
				String reason = getBanReason(args);
				System.out.println(args[1]+": uuid Is Curently Banned For: "+ reason);
			}
			else if (!isBanned) {
				if(getConfig().isSet("Banned_UUIDs." + uuid + ".Reason")) {
					String reason = getBanReason(args);
					System.out.println(args[1]+" Used To Be Banned For: \""+reason+"\"But They Where Unbanned");
				}
				if(getConfig().isSet("Banned_UUIDs." + uuid + ".UnbanReason")) {
					String unbanReason = getUnbanReason(args);
					System.out.println(args[1]+" Was Unbanned For: "+ unbanReason);
				}	
			}
		}
		else if(argument.equalsIgnoreCase("BanCheck") && args.length < 2) {
			System.out.println("Usage: /uuid config (Username)");
		}
		else if(argument.equalsIgnoreCase("Config") && args.length >= 2) {
			configSwitch(sender, args);
		}
		else if(argument.equalsIgnoreCase("Config") && args.length < 2) {
			System.out.println("Usage: /uuid config (Setting) (Option)");
			
		}
		else {
			System.out.println("Use /uuid Help  - For help");
		}
		
		return true;
	}
	
	public void ban(String[] args) {
		String uuid = getUuid(args[1]);
		String reason = ChatColor.translateAlternateColorCodes('&', arrToString(args,2));
		if (addBan(uuid,args[1],reason) == true) {
			System.out.println(ChatColor.stripColor(getFormat("BanFormat",args[1],reason,uuid)));
			for(Player p : Bukkit.getOnlinePlayers()) {
				if(p.hasPermission(PlayerCheck)||p.hasPermission(PlayerBan)||p.hasPermission(FormatEdit)||p.isOp()) {
					p.sendMessage(getFormat("BanFormat",args[1],reason,uuid));
				}
			}
		}
	}
	
	public boolean changeConfig(CommandSender sender, String[] args, String change) {
		if(args.length > 2) {
			String string = arrToString(args,2);
			string = ChatColor.translateAlternateColorCodes('&', string);
			getConfig().set(change, string);
			saveConfig();
			dynMessage(sender,change+ChatColor.GOLD+" Has Been Set to "+ChatColor.GREEN+string);
			return true;
		}
		dynMessage(sender,ChatColor.RED+"Edit Failed, Either Config Field Does Not Exist, Or Invalad Text Was Given");
		return false;
	}
	
	public boolean configSwitch(CommandSender sender, String[] args) {
		String s = args[1];
		switch (s.toLowerCase()){
		case "help": dynMessage(sender,ChatColor.GOLD+"Help Not Implemented Yet");
		return true;
		case "prefix": changeConfig(sender,args,"Kick_Prefix");
		return true;
		case "banformat":changeConfig(sender,args,"BanFormat");
		return true;
		case "checkformat":changeConfig(sender,args,"CheckFormat");
		return true;
		case "unbanformat":changeConfig(sender,args,"UnbanFormat");
		return true;
		case "unbanwreasonformat":changeConfig(sender,args,"UnbanWReasonFormat");
		return true;
		case "banreasonformat":changeConfig(sender,args,"BanReasonFormat");
		return true;
		case "pastbanreasonformat":changeConfig(sender,args,"pastbanreasonformat");
		return true;
		case "unbanreasonformat": changeConfig(sender,args,"UnbanReasonFormat");
		return true;
		case "notbannedformat": changeConfig(sender,args,"NotBannedFormat");
		return true;
		default:dynMessage(sender,"Usage: "+ChatColor.GOLD+"/uuid config (Setting) (Option)");
		return true;
		}
	}
	
	public String getFormat(String path, String first, String second, String third) {
		String toFormat = getConfig().getString(path);
		String string = toFormat.replace("!", first);
		string = string.replace("@", second);
		string = string.replace("#", third);
		return string;
	}
	
	public String getBanReason(String[] args) {
		String uuid = getUuid(args[1]);
		String reason =(getConfig().getString("Banned_UUIDs." + uuid + ".Reason"));
		return reason;
	}
	
	public String getUnbanReason(String[] args) {
		String uuid = getUuid(args[1]);
		if(getConfig().isSet("Banned_UUIDs." + uuid + ".UnbanReason")) {
			String unbanReason = getConfig().getString("Banned_UUIDs." + uuid + ".UnbanReason");
			return unbanReason;
		}
		return null;
	}
	
	public boolean banCheck(String[] args) {
		String uuid = getUuid(args[1]);
		if(getConfig().isSet("Banned_UUIDs." + uuid)&&getConfig().getBoolean("Banned_UUIDs." + uuid + ".Banned") == true) {
			return true;
		}
		return false;
		
	}
	
	public void unBan(CommandSender sender, String[] args) {
		String uuid = getUuid(args[1]);
		getConfig().set("Banned_UUIDs." + uuid + ".Banned", false);
		if(args.length == 2) {
			dynMessage(sender,getFormat("UnbanFormat",args[1],"",""));
			getConfig().set("Banned_UUIDs." + uuid + ".UnbanReason",null);
		}
		else if(args[2] != null) {
			String str = arrToString(args,2);
			dynMessage(sender,getFormat("UnbanWReasonFormat",args[1],str,""));
			getConfig().set("Banned_UUIDs." + uuid + ".UnbanReason", str);
		}
		saveConfig();
	}
		 
	public String arrToString(String[] arr, int skip) {
		StringBuilder b = new StringBuilder();
		for(int x = skip; x<arr.length; x++) {
		    b.append(arr[x]+" ");
		}
		return b.toString();
	}
	
	@SuppressWarnings("unchecked")
	public boolean addBan(String uuid, String toBan, String reason) {
		String prefix = ChatColor.translateAlternateColorCodes('&', getConfig().getString("Kick_Prefix"));
		if(Bukkit.getServer().getPlayer(toBan) != null) {
			Player player = (Player) Bukkit.getServer().getPlayer(toBan);
			player.kickPlayer(prefix+ChatColor.WHITE+reason);
		}
			
		getConfig().set("Banned_UUIDs." + uuid + ".Banned", true);
		getConfig().set("Banned_UUIDs." + uuid + ".Reason", reason);
		
		
		ArrayList<String> IDs = new ArrayList<String>();
		if(!getConfig().isSet("Banlist")) {
			getConfig().set("List", IDs);
		}
		IDs = (ArrayList<String>) getConfig().getList("Banlist");
		IDs.remove(uuid);
		IDs.add(uuid);
		getConfig().set("List", IDs);
		getConfig().set("Banned_Names."+ toBan, uuid);
		saveConfig();
		return true;
	}
	
@EventHandler
	public void onPlayerJoin(PlayerJoinEvent e) {
		
		Player player = (Player) e.getPlayer();
		if(getConfig().isSet("Banned_Names." + player.getName()) && (!player.hasPermission(PlayerCheck)||!player.hasPermission(PlayerBan)||!player.hasPermission(FormatEdit)||!player.hasPermission(UnBannable)||!player.isOp())){
			String uuid = getUuid(player.getName());
			System.out.println(uuid+" joined and was checked for a uuid ban");
			if(getConfig().isSet("Banned_UUIDs." + uuid + ".Banned") == true && getConfig().getBoolean("Banned_UUIDs." + uuid + ".Banned") == true) { 
				String prefix = getConfig().getString("Kick_Prefix");
				String reason =getConfig().getString("Banned_UUIDs." + uuid + ".Reason");
				System.out.println("uuid Ban Found"+"Kicking: " + player +" uuid: "+ uuid +" For:"+reason);
				prefix = ChatColor.translateAlternateColorCodes('&', prefix);
				reason = ChatColor.translateAlternateColorCodes('&', reason);
				player.kickPlayer(prefix+ChatColor.WHITE+reason);
				
				Bukkit.getServer().getPluginManager().callEvent(new EnforcerEvent(player, Type.KICK));
			}
		}
	}

}